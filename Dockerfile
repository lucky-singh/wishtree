FROM python:3.6-slim-jessie

USER root

# --------------------
# INSTALL OS PACKAGES
# --------------------
RUN apt-get install -y libpq-dev

# ---------------------
# CONFIG DIRS IN OS
# ---------------------
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN chmod -R a+rx /usr/src/app/

# ------------------------
# Set Enviornment variable1
# ------------------------
ENV FLASK_APP=app.py
ENV DATABASE_URL='sqlite:///wishtree.db'

# ------------------------
# Install app dependencies
# ------------------------

# private ngv repos
# RUN pip2 install git+https://GITHUB_AUTH_KEY:x-oauth-basic@github.com/REPO_PATH/REPO#egg=my_lib_name
RUN pip install -r requirements.txt

# Indicate what port needs to be mapped by the docker daemon
EXPOSE 5000

# ------------------------
# RUN APP
# ------------------------
# Define the command to start the app
CMD /bin/bash -c "python app.py && gunicorn --config=gunicorn.py app:app"