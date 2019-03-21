from . import db
from . import ma

# Modèles
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    bio = db.Column(db.String(200))

    def __init__(self, name, bio):
        self.name = name
        self.bio = bio

class ArtistSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'bio')

# init schema
artist_schema = ArtistSchema(strict=True)
artists_schema = ArtistSchema(many=True, strict=True)
