Getting started
===============

Setup virtualenv and install requirements:

    virtualenv --no-site-packages .
    source bin/activate
    pip install -r dev_requirements.txt

Create kepler/local_settings.example.py and set any personal preferences:

    cp kepler/local_settings.example.py kepler/local_settings.py

Create the initial database:

    python kepler/manage.py syncdb

Run the development server:

    python kepler/manage.py runserver

Go to http://127.0.0.1:8000/
