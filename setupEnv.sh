#!/bin/sh

# Setup python environment
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

# Setup React environment
cd react-src
npm install

# Cleanup
deactivate