from flask import Flask, Blueprint, request, jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from music_pycolore import db, ma
from .models import *

api = Blueprint("api", __name__)

# Création artiste
@api.route("/artistes", methods=["POST"])
def add_product():
    data = {"name": request.json["name"], "bio": request.json["bio"]}

    new_artist = Artist(**data)

    db.session.add(new_artist)
    db.session.commit()

    return artist_schema.jsonify(new_artist)

# Liste des artistes
@api.route("/artistes", methods=["GET"])
def products():
    pass