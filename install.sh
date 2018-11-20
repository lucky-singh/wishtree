#!/usr/bin/env bash

sudo apt update -y
sudo apt install -y python nginx supervisor python-pip virtualenv git

sudo rm /etc/nginx/sites-enabled/default

sudo cat <<EOT >> flask_settings
server {
        location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header Host \$host;
                proxy_set_header X-Real-IP \$remote_addr;
        }
}
EOT

sudo mv flask_settings /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/flask_settings /etc/nginx/sites-enabled/
sudo /etc/init.d/nginx restart

git clone https://github.com/lucky-singh/wishtree.git
cd wishtree

virtualenv venv
source venv/bin/activate

pip install -r requirements.txt

export FLASK_APP=app.py
export FLASK_ENV=development
export DATABASE_URL="postgres://wishtree:1qw21qw2@pg.c6xznrtkhl6g.us-east-1.rds.amazonaws.com:5432/wishtree"

gunicorn app:app

