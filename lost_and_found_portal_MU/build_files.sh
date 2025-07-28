#!/bin/bash
set -e

# Create and activate virtual environment
python3.9 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python3.9 manage.py collectstatic --noinput --clear
