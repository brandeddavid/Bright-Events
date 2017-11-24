#app/__init__.py

from flask import Flask

#Initialize app

app = Flask(__name__, instance_relative_config=True)

#Import the views

from app import views

#Load the config file

app.config.from_object('config')
