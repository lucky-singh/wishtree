#!/usr/bin/env bash

# Repo location
#git clone https://github.com/lucky-singh/wishtree.git && cd wishtree

sudo apt update -y
sudo apt install -y python python-pip virtualenv git

# Nginx configuration

sudo cat <<EOT >> flask_settings
server {
        location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header Host \$host;
                proxy_set_header X-Real-IP \$remote_addr;
        }
}
EOT

sudo mv /etc/nginx/sites-enabled/default /etc/nginx/sites-enabled/default.original
sudo mv flask_settings /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/flask_settings /etc/nginx/sites-enabled/
sudo /etc/init.d/nginx restart

virtualenv venv
source venv/bin/activate

pip install -r requirements.txt

export FLASK_APP=app.py
export DATABASE_URL='sqlite:///wishtree.db'

python app.py

gunicorn -b 127.0.0.1:8000 app:app