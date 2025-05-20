import logging

from ..utils.mcp_app import ChemMCPManager, run_mcp_server
from ..tool_utils.property_prediction import PropertyPredictor


logger = logging.getLogger(__name__)


@ChemMCPManager.register_tool
class LogDPredictor(PropertyPredictor):
    __version__ = "0.1.0"
    name = "LogDPredictor"
    func_name = 'predict_logd'
    description = 'Predict the logD of a molecule given its SMILES representation.'
    categories = ["Molecule"]
    tags = ["Molecular Information", "Molecular Properties", "SMILES", "Neural Networks"]
    required_envs = []
    code_input_sig = [('smiles', 'str', 'N/A', 'SMILES string of the molecule.')]
    text_input_sig = [('smiles', 'str', 'N/A', 'SMILES string of the molecule.')]
    output_sig = [('logd', 'str', 'The octanol/water distribution coefficient logD under the circumstance of pH 7.4.')]
    examples = [
        {'code_input': {'smiles': 'NC(=O)C1=CC=CC=C1O'}, 'text_input': {'smiles': 'NC(=O)C1=CC=CC=C1O'}, 'output': {'logd': 'The octanol/water distribution coefficient logD under the circumstance of pH 7.4 is 1.090.\nNote that the result is predicted by a neural network model and may not be accurate. You may use other tools or resources to obtain more reliable results if needed.'}},
    ]

    def __init__(
        self, 
        init=True, 
        interface='code'
    ):
        super().__init__('lipo', init, interface=interface)

    def _run_base(self, smiles: str) -> str:
        r = super()._run_base(smiles)
        return 'The octanol/water distribution coefficient logD under the circumstance of pH 7.4 is {:.3f}.'.format(r) + '\nNote that the result is predicted by a neural network model and may not be accurate. You may use other tools or resources to obtain more reliable results if needed.'


if __name__ == "__main__":
    run_mcp_server()
