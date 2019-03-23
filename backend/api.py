from flask import Flask, Blueprint, request, jsonify, current_app
from flask.views import View
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from . import db, ma
from .models import Artist, artist_schema, artists_schema

api = Blueprint("api", __name__)


# Liste des artistes
@api.route("/artistes", methods=["GET"])
def artists():
    pass


# Liste des albums
@api.route("/albums", methods=["GET"])
def albums():
    pass


# Liste des chansons
@api.route("/chansons", methods=["GET"])
def songs():
    pass