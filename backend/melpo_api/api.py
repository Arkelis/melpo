from flask import Blueprint, request, jsonify, abort, Response
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
        schema_name = f"{self.model.__name__.lower()}" + ("s" if many else "") + "_schema"
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

# func from Flask docs to refactor
def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    api.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    api.add_url_rule(url, view_func=view_func, methods=['POST',])
    api.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                     methods=['GET', 'PATCH', 'DELETE'])

register_api(ArtistAPI, 'artist_api', '/artistes/')
register_api(AlbumAPI, 'album_api', '/albums/')
register_api(SongAPI, 'song_api', '/titres/')

# scan des fichiers
@api.route("/scan")
def scan_library():
    scan()


# Erreurs
@api.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400
