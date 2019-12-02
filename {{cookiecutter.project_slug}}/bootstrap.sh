#!/bin/bash

set -ex

PYTHON_VERSION={{ cookiecutter.python_version }
VIRTUALENV_NAME={{ cookiecutter.project_name }}-${PYTHON_VERSION}

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv install -s ${PYTHON_VERSION}
if [ ! -e "${PYENV_ROOT}/versions/${VIRTUALENV_NAME}" ]; then
    pyenv virtualenv ${PYTHON_VERSION} ${VIRTUALENV_NAME}
fi
pyenv activate ${VIRTUALENV_NAME}
pip install --upgrade pip
pip install -e .
pip install -r requirements-dev.txt
pip install -r requirements-test.txt
pre-commit install
