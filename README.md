kepler-explorer
===============

Getting started
===============

Setup virtualenv and install requirements

virtualenv --no-site-packages .
source bin/activate
pip install -r dev_requirements.txt

python kepler/manage.py syncdb

python kepler/manage.py runserver

Go to http://127.0.0.1:8000/
