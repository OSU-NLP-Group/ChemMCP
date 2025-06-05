# ChemMCP

<img src="site/assets/img/icon_text_logo.png" alt="ChemMCP Banner" style="zoom:20%;" />

See our website and document at [osu-nlp-group.github.io/ChemMCP](https://osu-nlp-group.github.io/ChemMCP/).

## What is this?

ChemMCP is **a continuously updated collection of chemistry tools for LLMs and AI assistants**, compatible with the [Model Context Protocol (MCP)](https://modelcontextprotocol.org/). By integrating **powerful chemistry tools**, ChemMCP **transforms general AI models into chemistry coscientists** capable of performing complex molecular analysis, property prediction, and reaction synthesis tasks without requiring domain-specific training.

[MCP (Model Context Protocol)](https://modelcontextprotocol.io/introduction) is a framework that allows AI models to access external tools and resources through a standardized interface. ChemMCP leverages this architecture to bridge the gap between general-purpose AI models and specialized chemistry tools, enabling seamless integration of chemistry expertise into AI workflows.

Specifically, ChemMCP provides the following key features:

- **🔌 Plug-and-Play Chemistry for AI Assistants**: ChemMCP can be integrated into any [MCP-enabled LLM clients](https://github.com/punkpeye/awesome-mcp-clients) in just minutes, allowing researchers to augment LLMs with chemistry capabilities without additional training.
- **🛠️ Standalone Toolkit for Custom Workflows**: With its decoupled design and unified interfaces, [ChemMCP tools](https://osu-nlp-group.github.io/ChemMCP/tools) can be easily imported into your workflow, to process data, assemble pipeline steps, or build bespoke agentic applications — via MCP or Python, whichever you prefer.
- **🤖 Native RL Agent Framework**: ChemMCP natively supports multi-turn interactive loops between agents and tool, providing an ideal infrastructure and testbed for scientific tool-using agents.
- **📦 Modular and Extensible Design**: Adding a new tool is as simple as writing a Python file (see [here](https://osu-nlp-group.github.io/ChemMCP/dev-guide/)). All tools follow a consistent schema, ensuring clear interfaces, easy maintenance, and automatic documentation.

We will continue to add and maintain tools in ChemMCP. **You are more than welcome to contribute, such as giving us your feedback, maining existing tools, or adding new tools!**

## Get Started

[This document](https://osu-nlp-group.github.io/ChemMCP/get-started/) will help you quickly set up and start using ChemMCP.

## Tool List

Based on the functions, the tools can be divided into general tools, molecule tools, and reaction tools:

- **General Tools**: Provide broad information retrieval and web searching.
- **Molecule Tools**: Offer various analyses, predictions, and conversions related to chemical compounds and their properties.
- **Reaction Tools**: Predict products of chemical reactions and suggest potential reactants for synthesizing given products.

Check the updated full list of tools [here](https://osu-nlp-group.github.io/ChemMCP/tools/).

## Citation

If ChemMCP is valuable to your research or development, please kindly cite our work.

```
@misc{yu2025chemmcp,
  author       = {Botao Yu and Huan Sun},
  title        = {ChemMCP: A Chemistry MCP Toolkit},
  year         = {2025},
  url          = {https://github.com/OSU-NLP-Group/ChemMCP},
  note         = {2025-04-28-01},
}

@article{yu2024chemtoolagent,
    title={ChemToolAgent: The Impact of Tools on Language Agents for Chemistry Problem Solving},
    author={Botao Yu and Frazier N. Baker and Ziru Chen and Garrett Herb and Boyu Gou and Daniel Adu-Ampratwum and Xia Ning and Huan Sun},
    journal={arXiv preprint arXiv:2411.07228},
    year={2024}
}
```


## Ethical and Resonsible Use Statement

ChemMCP is an open-source toolkit that integrates language models and agents with chemistry tools and publicly available chemical data to support AI for Science research. While ChemMCP offers powerful capabilities, it is essential to acknowledge potential risks associated with its use.

1. **Safety and Responsibility**

   ChemMCP includes a safety-check tool designed to help identify hazardous molecules; however, the toolkit itself does not enforce its use. Because ChemMCP is not a standalone agent but rather an open-source resource, we cannot guarantee that every user will employ safety measures.

   Large language models paired with ChemMCP often incorporate their own safety mechanisms, which typically refuse requests involving illegal or unethical applications. Nonetheless, users bear full responsibility for ensuring that all activities comply with applicable safety protocols and legal requirements.

   As ChemMCP accesses only publicly available tools and data, we disclaim liability for any dangerous or illicit use. Users must verify that their workflows are safe, lawful, and ethically sound.

2. **Intended Use**

   ChemMCP is provided solely for legitimate research, educational, and investigative purposes.

   Under no circumstances should ChemMCP be used to design, manufacture, or recommend harmful substances (e.g., chemical toxins or weapons). Any attempt to exploit the toolkit for malicious ends violates our terms and ethical guidelines.

3. **Limitations and Disclaimer**

   ChemMCP does not guarantee the accuracy, completeness, or safety of its outputs. All computations and inferences are provided “as is,” without warranties of any kind.

   We are not liable for any direct or indirect consequences—financial, legal, or otherwise—that arise from using ChemMCP. Users should independently validate results before applying them in critical or hazardous contexts.

4. **Contributions and Safeguards**

   We encourage community contributions that enhance ChemMCP’s safety features and promote responsible use. Contributors must document any identified risks, potential failure modes, and mitigation strategies when introducing new tools or data sources.

   Before merging new functionality, maintainers should review proposed changes for possible misuse scenarios and update documentation accordingly.

5. **User Agreement**

   By installing or invoking ChemMCP, you agree to:

   1. Use the toolkit in compliance with all applicable laws, regulations, and institutional policies.
   2. Apply reasonable safety checks—both human and automated—when handling potentially hazardous data or compounds.
   3. Refrain from any activity that could facilitate the creation, distribution, or use of harmful substances.
   4. Accept full responsibility for your use of ChemMCP and any outcomes that result from its deployment.

## License

ChemMCP is distributed under the [Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/). The toolkit’s implementation depends heavily on open-source projects—most notably [RDKit](https://github.com/rdkit/rdkit) (BSD 3-Clause) and the [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) (MIT). Additional main open-source dependencies (whose code is used in whole or in part) and any required hosted services or software are listed in the table below. By using ChemMCP and its tools, you agree to comply with all referenced licenses and terms of service.

| Tool Name               | **Primary Open-Source Dependencies** | Hosted Service / Software |
|-------------------------|-------|-------|
| BbbpPredictor          | [Uni-Mol](https://github.com/deepmodeling/Uni-Mol) (MIT), [Uni-Core](https://github.com/dptech-corp/Uni-Core) (MIT) |  |
| ForwardSynthesis       | [ChemCrow](https://github.com/ur-whitelab/chemcrow-public) (MIT), [rxn4chemistry](https://github.com/rxn4chemistry/rxn4chemistry) (MIT) | [IBM RXN for Chemistry](https://rxn.app.accelerate.science/) |
| FunctionalGroups       | [ChemCrow](https://github.com/ur-whitelab/chemcrow-public) (MIT) |       |
| HivInhibitorPredictor  | [Uni-Mol](https://github.com/deepmodeling/Uni-Mol) (MIT), [Uni-Core](https://github.com/dptech-corp/Uni-Core) (MIT) |       |
| Iupac2Smiles           | [ChemCrow](https://github.com/ur-whitelab/chemcrow-public) (MIT), [molbloom](https://github.com/whitead/molbloom) (MIT), [PubChemPy](https://github.com/mcs07/PubChemPy) (MIT) | [PubChem](https://pubchem.ncbi.nlm.nih.gov/), [ChemSpace](https://chem-space.com/) |
| LogDPredictor          | [Uni-Mol](https://github.com/deepmodeling/Uni-Mol) (MIT), [Uni-Core](https://github.com/dptech-corp/Uni-Core) (MIT) |       |
| MoleculeAtomCount      | [ChemCrow](https://github.com/ur-whitelab/chemcrow-public) (MIT) |       |
| MoleculeCaptioner      | [MolT5](https://github.com/blender-nlp/MolT5) (BSD 3-Clause) |       |
| MoleculeGenerator      | [MolT5](https://github.com/blender-nlp/MolT5) (BSD 3-Clause) |       |
| MoleculeModifier       | [synspace](https://github.com/whitead/synspace) (MIT) |       |
| MoleculePrice          | [ChemCrow](https://github.com/ur-whitelab/chemcrow-public) (MIT) | [ChemSpace](https://chem-space.com/) |
| MoleculeSimilarity     | [ChemCrow](https://github.com/ur-whitelab/chemcrow-public) (MIT) |       |
| MoleculeSmilesCheck    |       |       |
| MoleculeVisualizer     |       |       |
| MoleculeWeight         |       |       |
| Name2Smiles            | [PubChemPy](https://github.com/mcs07/PubChemPy) (MIT) |       |
| PatentCheck           | [molbloom](https://github.com/whitead/molbloom) (MIT) |       |
| PubchemSearch         |       | [PubChem](https://pubchem.ncbi.nlm.nih.gov/) |
| PubchemSearchQA       |       | [PubChem](https://pubchem.ncbi.nlm.nih.gov/), Custom LLMs |
| PythonExecutor        | [Jupyter Notebook](https://github.com/jupyter/notebook) (BSD 3-Clause) | [docker](https://www.docker.com/) |
| ReactionSmilesCheck   |       |       |
| Retrosynthesis        | [ChemCrow](https://github.com/ur-whitelab/chemcrow-public) (MIT), [rxn4chemistry](https://github.com/rxn4chemistry/rxn4chemistry) (MIT) | [IBM RXN for Chemistry](https://rxn.app.accelerate.science/) |
| SafetyCheck           | [ChemCrow](https://github.com/ur-whitelab/chemcrow-public) (MIT) | [PubChem](https://pubchem.ncbi.nlm.nih.gov/), Custom LLMs |
| Selfies2Smiles        | [selfies](https://github.com/aspuru-guzik-group/selfies) (Apache License 2.0) |       |
| SideEffectPredictor   | [Uni-Mol](https://github.com/deepmodeling/Uni-Mol) (MIT), [Uni-Core](https://github.com/dptech-corp/Uni-Core) (MIT) |       |
| Smiles2Cas            | [ChemCrow](https://github.com/ur-whitelab/chemcrow-public) (MIT) | [PubChem](https://pubchem.ncbi.nlm.nih.gov/) |
| Smiles2Formula        |       | [PubChem](https://pubchem.ncbi.nlm.nih.gov/) |
| Smiles2Iupac          | [PubChemPy](https://github.com/mcs07/PubChemPy) (MIT) | [PubChem](https://pubchem.ncbi.nlm.nih.gov/) |
| Smiles2Selfies        | [selfies](https://github.com/aspuru-guzik-group/selfies) (Apache License 2.0) |       |
| SmilesCanonicalization| [LlaSMol](https://github.com/OSU-NLP-Group/LLM4Chem) (MIT) |       |
| SolubilityPredictor   | [Uni-Mol](https://github.com/deepmodeling/Uni-Mol) (MIT), [Uni-Core](https://github.com/dptech-corp/Uni-Core) (MIT) |       |
| ToxicityPredictor     | [Uni-Mol](https://github.com/deepmodeling/Uni-Mol) (MIT), [Uni-Core](https://github.com/dptech-corp/Uni-Core) (MIT) |       |
| WebSearch            | [tavily-python](https://github.com/tavily-ai/tavily-python) (MIT) | [Tavily](https://www.tavily.com/) |

**Notes**:

- Any open-source software dependency not explicitly identified in the table above—including any indirect or transitive dependencies introduced by packages such as RDKit or PyTorch—remains subject to the terms of its own license. For a complete inventory of all dependencies and their corresponding license obligations, users should consult the project’s requirements.txt file or employ a license-compliance utility (for example, pip-licenses).
- Hosted services and application programming interfaces (APIs) referenced herein—for instance, IBM RXN for Chemistry, PubChem, or externally hosted language models—are each governed by their own Terms of Service, Acceptable Use Policies, or equivalent contractual agreements. Users are responsible for reviewing and adhering to all applicable terms and conditions imposed by the providers of these external services.
