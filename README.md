# Azure Synapse Notebook Tests

This repository contains 2 workflows:

- **Notebook Linting & Unit Tests** (`unit-tests.yml`): runs `pylint` and unit tests for the notebooks in the `workspace/notebooks` folder
- **Synapse Workspace Deployment** (`workspace-deployment.yml`): creates the templates for the Synapse workspace.

## Notebook Linting & Unit Tests

### Prerequisites:

- [nbQA](https://github.com/nbQA-dev/nbQA): Run isort, pyupgrade, mypy, pylint, flake8, black, blacken-docs, and more on Jupyter Notebooks
- [testbook](https://github.com/nteract/testbook): Unit test your Jupyter Notebooks.

### How it works

The workflow usese github actions to preform the following steps:

- Checks out the code.
- Installs [nbQA](https://github.com/nbQA-dev/nbQA) & [testbook](https://github.com/nteract/testbook).
- Extracts and fixes the `ipynb` notebooks from the `workspace/notebooks` folder. Resulting files are stored in the `ipynb_to_test` folder.
- Using [nbQA](https://github.com/nbQA-dev/nbQA) runs `pylint` on the `ipynb_to_test` folder.
- Using [testbook](https://github.com/nteract/testbook) run `pytest` on the `ipynb_to_test` folder.

## Synapse Workspace Deployment

### How it works

The workflow uses github actions to preform the following steps:

- Checks out the code.
- Runs the validate operation of the `Azure/Synapse-workspace-deployment` action.
- Uploads the template files created in th `ExportedArtifacts` folder as artifacts.

## References

- [Automating the Publishing of Workspace Artifacts in Synapse CICD](https://techcommunity.microsoft.com/t5/azure-synapse-analytics-blog/automating-the-publishing-of-workspace-artifacts-in-synapse-cicd/ba-p/3603042)
- [Continuous integration and delivery for an Azure Synapse Analytics workspace](https://learn.microsoft.com/en-us/azure/synapse-analytics/cicd/continuous-integration-delivery#set-up-a-release-in-github-actions)
- [Azure Synapse Workspace Deployment](https://github.com/Azure/Synapse-workspace-deployment)
- [nbQA](https://github.com/nbQA-dev/nbQA)
- [testbook](https://github.com/nteract/testbook)