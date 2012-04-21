Getting started
===============

Setup virtualenv and install requirements:

    virtualenv --no-site-packages .
    source bin/activate
    pip install -r dev_requirements.txt

Create kepler/local_settings.example.py and set any personal preferences:

    cp kepler/local_settings.example.py kepler/local_settings.py

Create the initial database:

    python manage.py syncdb

Import data

    curl -O http://exoplanets.org/exoplanets.csv
	python manage.py celestial_import exoplanets.csv

Run the development server:

    python manage.py runserver

Go to http://127.0.0.1:8000/
