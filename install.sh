#!/usr/bin/env bash

# Repo location
#git clone https://github.com/lucky-singh/wishtree.git && cd wishtree

sudo apt update -y
sudo apt install -y python python-pip virtualenv git


virtualenv venv
source venv/bin/activate

pip install -r requirements.txt

export FLASK_APP=app.py
export FLASK_ENV=development

python app.py

flask run