# Kepler Explorer #

## The challenge ##

This is a solution to the http://spaceappschallenge.org/ Open Data Challenge -- Kepler: 

The challenge is to help NASA either a) make Kepler data more accessible or b) create something amazing with it. It could be an app that better visualizes the data, an interface that presents the data in a new way, an infographic that helps understand the data in a new way, or more.

http://spaceappschallenge.org/challenge/open-data-challenge-kepler/

## The solution ##

A webapp designed for classroom use to allow children and teachers to explore all the exoplanets that we know about.

http://www.planethopper.co.uk/

http://spaceappschallenge.org/challenge/open-data-challenge-kepler/solution/47

The project is written in the Python framework Django.

## Getting started ##

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
