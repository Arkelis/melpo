from flask import Blueprint, request, jsonify, abort, Response, send_file
import requests
import shutil
import sys
import os
from flask.views import MethodView
from . import db
from .models import Artist, Album, Song
from .models import artist_schema, artists_schema, album_schema, albums_schema, song_schema, songs_schema
from .scan import scan

api = Blueprint("api", __name__)

@api.route("/")
def index():
    return "This is Melpo API's index."


class BaseAPI(MethodView):
    """Base view for listing and posting instances of the given model.
    
    Derive this view to use it and give it your model. It will look for
    <yourmodel>_schema object and use it as its schema (you must import
    it if it is not defined in the current module). Otherwise you
    can assign the schema object to schema variable.
    """

    model = None # assign a model in derived view
    schema = None # optionally assign a schema in derived view
    schema_many = None # optionally assign a schema in derived view    

    def __init__(self):
        if not self.schema:
            self.init_schema()
        if not self.schema_many:
            self.init_schema(many=True)

    def init_schema(self, many: bool = False):
        name = "schema_many" if many else "schema"
        schema_name = self.model.__name__.lower() + ("s" if many else "") + "_schema"
        if schema_name in globals():
            setattr(self, name, eval(schema_name))
        else:
            raise AttributeError(
                f"You must provide a schema as {schema_name} was not found."
            )    

    def get(self, id):
        if not id:
            instances = self.model.query.all()
            return self.schema_many.jsonify(instances)
        else:
            instance = self.model.query.get_or_404(id)
            return self.schema.jsonify(instance)

    def post(self):
        try:
            deserialized_result = self.schema.load(request.json)
            db.session.add(deserialized_result.data)
            db.session.commit()
        except Exception as err:
            print(type(err), err)
            abort(400)
        return self.schema.jsonify(deserialized_result.data), 204    

    def patch(self, id):
        instance_to_patch = self.model.query.get_or_404(id)
        for name, value in request.json.items():
            setattr(instance_to_patch, name, value)
        db.session.add(instance_to_patch)
        db.session.commit()
        return self.schema.jsonify(instance_to_patch)

    def delete(self, id):
        instance_to_delete = self.model.query.get_or_404(id)
        db.session.delete(instance_to_delete)
        db.session.commit()
        return jsonify({"success": f"<{self.model.__name__}: {id}> has been deleted from database."})        


class ArtistAPI(BaseAPI):
    model = Artist

class AlbumAPI(BaseAPI):
    model = Album

class SongAPI(BaseAPI):
    model = Song

def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    api.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=['GET'])
    api.add_url_rule(url, view_func=view_func, methods=['POST'])
    api.add_url_rule(f"{url}<{pk_type}:{pk}>", view_func=view_func, methods=['GET', 'PATCH', 'DELETE'])

register_api(ArtistAPI, 'artist_api', '/artists/')
register_api(AlbumAPI, 'album_api', '/albums/')
register_api(SongAPI, 'song_api', '/songs/')

# scan des fichiers
@api.route("/scan")
def scan_library():
    artists = [artist.name for artist in Artist.query.all()]
    albums = [album.name for album in Album.query.all()]
    songs = [song.path for song in Song.query.all()]
    found_data = scan()

    # First iteration: find new artists
    for song in found_data:
        if not song["artist"]:
            continue
        if song["artist"] not in artists:
            new_artist = Artist(name=song["artist"])
            artists.append(new_artist.name)
            db.session.add(new_artist)
    db.session.commit()

    # Second iteration: find new albums
    for song in found_data:
        if not song["album"]:
            continue
        if song["album"] not in albums:
            new_album = Album(name=song["album"])
            albums.append(new_album.name)
            db.session.add(new_album)
    db.session.commit()

    # Last iteration: commit songs
    for song in found_data:
        if song["path"] in songs:
            continue
        new_song = Song(
            title=song["title"],
            length=song["length"],
            path = song["path"],
            track_number = song["track_number"]
        )
        if song["album"]:
            new_song.album = Album.query.filter_by(name=song["album"]).first()
        if song["artist"]:
            new_song.artists.append(Artist.query.filter_by(name=song["artist"]).first())
        db.session.add(new_song)
        print(f"Ajout de {song['title']}")
    db.session.commit()
    return jsonify("Scan was successful.")

@api.route("/image/<model_name>/<int:pk>")
def get_cover(model_name, pk):
    if model_name not in ("artist", "album"):
        return jsonify("Les images ne sont disponibles que pour les artistes ou les albums."), 404
    model = {
        "artist": Artist,
        "album": Album,
    }[model_name]
    model_instance = model.query.get_or_404(pk)
    image_attr = {
        Artist: "picture",
        Album: "cover",
    }[type(model_instance)]
    picture_url = getattr(model_instance, image_attr)
    if not picture_url:
        deezer_response = requests.get(f"https://api.deezer.com/search?q={model_name}:'{model_instance.name.lower()}'")
        try:
            deezer_picture_url = deezer_response.json()["data"][0][model_name][f"{image_attr}_xl"]
            deezer_response = requests.get(deezer_picture_url, stream=True)
            picture_url = str(os.getcwd()) + f"/img/{model_name}/{model_instance.id}.jpg"
            with open(picture_url, "wb") as picture:
                shutil.copyfileobj(deezer_response.raw, picture)
            setattr(model_instance, image_attr, picture_url)
            db.session.add(model_instance)
            db.session.commit()
        except IndexError:
            return jsonify("cover or picture not found")
    return send_file(picture_url, attachment_filename=f"{model_instance.name}.jpg")
    


# Erreurs
@api.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400
