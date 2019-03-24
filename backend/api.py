from flask import Blueprint, request, jsonify, abort, Response
from . import db
from .models import Artist, Album, Song
from .models import artist_schema, artists_schema, album_schema, albums_schema, song_schema, songs_schema

api = Blueprint("api", __name__)

@api.route("/")
def index():
    return "This is Melpo API's index."

# Liste des artistes
@api.route("/artistes", methods=["GET"])
def get_artists():
    artists = Artist.query.all()
    return artists_schema.jsonify(artists)


@api.route("/artistes", methods=["POST"])
def create_artist():
    try:
        artist = artist_schema.load(request.json)
        db.session.add(artist.data)
        db.session.commit()
    except Exception as err:
        print(type(err), err)
        abort(400)
    return artist_schema.jsonify(artist.data), 204
    

@api.route("/artistes/<id>", methods=["GET"])
def get_single_artist(id):
    artist = Artist.query.get_or_404(id)
    return artist_schema.jsonify(artist)

@api.route("/artistes/<id>", methods=["DELETE"])
def delete_artist(id):
    artist = Artist.query.get_or_404(id)
    db.session.delete(artist)
    db.session.commit()
    return jsonify({"success": f"<Artist: {id}> has been deleted from database."})

@api.route("/artistes/<id>", methods=["PATCH"])
def patch_artist(id):
    artist = Artist.query.get_or_404(id)
    for name, value in request.json.items():
        setattr(artist, name, value)
    db.session.add(artist)
    db.session.commit()
    return artist_schema.jsonify(artist)


# Liste des albums
@api.route("/albums", methods=["GET"])
def get_albums():
    albums = Album.query.all()
    return albums_schema.jsonify(albums)


# Liste des chansons
@api.route("/titres", methods=["GET"])
def get_songs():
    songs = Song.query.all()
    return songs_schema.jsonify(songs)


# Erreurs
@api.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400
