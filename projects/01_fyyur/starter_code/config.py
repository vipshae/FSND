import os, binascii; 
SECRET_KEY = binascii.hexlify(os.urandom(24))

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
FLASK_APP = 'app.py'
# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://vipsha@localhost:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False
