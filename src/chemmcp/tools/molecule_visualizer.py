import logging
from io import BytesIO

from mcp.server.fastmcp import Image
from rdkit import Chem
from rdkit.Chem import Draw

from ..utils.base_tool import BaseTool
from ..utils.errors import ChemMCPInputError
from ..utils.mcp_app import ChemMCPManager, run_mcp_server
from ..tool_utils.smiles import is_smiles


logger = logging.getLogger(__name__)


@ChemMCPManager.register_tool
class MoleculeVisualizer(BaseTool):
    __version__ = "0.1.0"
    name = "MoleculeVisualizer"
    func_name = 'visualize_molecule'
    description = "Visualize a molecule with RDKit."
    categories = ["Molecule"]
    tags = ["Molecular Information", "RDKit", "Visualization"]
    required_envs = []
    text_input_sig = [("smiles", "str", "N/A", "The SMILES string of the molecule.")]
    code_input_sig = [("smiles", "str", "N/A", "The SMILES string of the molecule.")]
    output_sig = [("result", "Image", "[The image of the molecule]")]
    examples = [
        {'text_input': {'smiles': 'C1=CC=CC=C1'}, 'code_input': {'smiles': 'C1=CC=CC=C1'}, 'output': {'result': '[Image]'}},
    ]

    def _run_base(self, smiles: str) -> tuple[str, Image, str]:
        if not is_smiles(smiles):
            raise ChemMCPInputError("Invalid SMILES string.")

        mol = Chem.MolFromSmiles(smiles)
        img = Draw.MolToImage(mol)

        buf = BytesIO()
        img.save(buf, format="PNG")
        png_bytes = buf.getvalue()

        text = f"The visualization of `{smiles}` is shown below."

        img = Image(
            data=png_bytes,
            format="png"
        )

        return (text, img, "above")


if __name__ == "__main__":
    run_mcp_server()
