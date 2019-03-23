"""This is Melpo, version 0.0.1 init file."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import os

CONFIG = {
    'DEBUG': True,
    'ENV': 'development'
} 

# init app
app = Flask(__name__)
app.config.from_mapping(**CONFIG)
basedir = os.path.abspath(os.path.dirname(__file__))

# database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db
db = SQLAlchemy(app)

# init migration engine
migrate = Migrate(app, db)

# init ma
ma = Marshmallow(app)

# index view
@app.route("/")
def index():
    return "This is Melpo Flask Backend!"

# register api
# import here to avoid import conflict
from .api import api
app.register_blueprint(api)