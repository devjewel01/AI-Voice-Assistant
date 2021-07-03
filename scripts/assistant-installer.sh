#!/bin/bash

set -o errexit

scripts_dir="$(dirname "${BASH_SOURCE[0]}")"
GIT_DIR="$(realpath $(dirname ${BASH_SOURCE[0]})/..)"


clear


sudo apt-get update -y
sed 's/#.*//' ${GIT_DIR}/Requirements/system-requirements.txt | xargs sudo apt-get install -y


echo ""
cd /home/${USER}/
python3 -m venv env
env/bin/python -m pip install --upgrade pip setuptools wheel
source env/bin/activate
pip install -r ${GIT_DIR}/Requirements/pip-requirements.txt




echo ""
echo "Finished installing your voice assistant......."
echo ""
echo "Please reboot........"
