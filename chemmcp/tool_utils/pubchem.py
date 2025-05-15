import requests
import logging

from ..utils.errors import *


logger = logging.getLogger(__name__)


def search_pubchem(keyword):
    keyword = keyword.replace(';', '%3B')
    url = 'https://pubchem.ncbi.nlm.nih.gov/sdq/sdqagent.cgi?infmt=json&outfmt=json&query={%22select%22:%22*%22,%22collection%22:%22compound%22,%22order%22:[%22relevancescore,desc%22],%22start%22:1,%22limit%22:10,%22where%22:{%22ands%22:[{%22*%22:%22' + keyword + '%22}]},%22width%22:1000000,%22listids%22:0}'
    data = requests.get(url).json()
    return data


def pubchem_iupac2cid(iupac, strict=False):
    iupac = iupac.replace('λ', 'lambda')
    data = search_pubchem(iupac)
    try:
        rows = data['SDQOutputSet'][0]['rows']
    except KeyError as e:
        raise ChemMTKSearchFailError("Cannot find a molecule/compound on PubChem that matches the input IUPAC name.") from e

    potential_cid = None
    if len(rows) > 0:  # If there are rows, meaning that there are some results
        potential_cid = rows[0]['cid']  # Use the first one as the last resort

        # Check if the IUPAC name matches anyone in the result
        matched_item = None
        iupac_lower = iupac.lower()
        for item in rows:
            try:
                if item['iupacname'].lower() == iupac_lower:
                    matched_item = item
                    break
            except KeyError:
                continue
        if matched_item is not None:
            return matched_item['cid']

    # if len(rows) == 0 or matched_item is None, check if each component of the IUPAC name
    parts = iupac.split(';')
    if len(parts) > 1:
        logger.info('The input IUPAC name contains multiple molecules/compounds. Searching for each of them.')
        parts_cid = []
        parts_cannot_find = []
        for part in parts:
            part = part.strip()
            try:
                cid = pubchem_iupac2cid(part)
            except ChemMTKSearchFailError:
                parts_cannot_find.append(part)
            else:
                parts_cid.append(cid)
        if len(parts_cannot_find) > 0:
            raise ChemMTKSearchFailError("Cannot find a molecule/compound for the following parts of the input IUPAC name: %s" % ', '.join(parts_cannot_find))
        else:
            return tuple(parts_cid)
    else:
        if potential_cid is not None:
            if strict:
                raise ChemMTKSearchFailError("Cannot find a molecule/compound that matches the input IUPAC name.")
            logger.info("Cannot find a molecule/compound that matches the input IUPAC name. Using the first matched one.")
            return potential_cid
        raise ChemMTKSearchFailError("Cannot find a molecule/compound on PubChem that matches the input IUPAC name. Possible reasons: 1) The input must be a valid IUPAC name. 2) Must input only one at a time. If you have multiple molecules to look up, please input each of them at a time.")


def pubchem_name2cid_old(name):
    data = search_pubchem(name)
    try:
        rows = data['SDQOutputSet'][0]['rows']
    except KeyError as e:
        raise ChemMTKSearchFailError("Cannot find a molecule/compound that matches the input IUPAC name.") from e

    if len(rows) > 0:
        if len(rows) > 1:
            logger.info("There are more than one molecules/compounds that match the input name. Using the first matched one.")
        return rows[0]['cid']
    else:
        raise ChemMTKSearchFailError("Cannot find a molecule/compound that matches the input name.")
    

def pubchem_name2cid(name):
    url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/' + name + '/cids/JSON'
    data = requests.get(url).json()
    try:
        cid = data['IdentifierList']['CID'][0]
    except KeyError as e:
        raise ChemMTKSearchFailError("Cannot find a molecule/compound that matches the input chemical name.") from e
    return cid
