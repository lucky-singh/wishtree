#!/usr/bin/env bash

# Repo location
#git clone https://github.com/lucky-singh/wishtree.git && cd wishtree

apt update -y
apt install -y python python-pip virtualenv git

virtualenv venv
source venv/bin/activate

pip install -r requirements.txt

export FLASK_APP=app.py
export DATABASE_URL='sqlite:///wishtree.db'

python app.py

gunicorn -b 0.0.0.0:5000 app:app
