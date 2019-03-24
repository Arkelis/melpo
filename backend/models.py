from . import db
from . import ma
from marshmallow import fields, post_load

# Modèles
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    bio = db.Column(db.Text(200))

    def __repr__(self):
        return f"Artist(name={self.name}, bio={self.bio})"

    def __str__(self):
        return self.name


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    year = db.Column(db.Integer)
    artist_id = db.Column(db.Integer, db.ForeignKey("artist.id"), nullable=False)
    artist = db.relationship("Artist", backref=db.backref("albums", lazy=True))

    def __repr__(self):
        return f"Album(name={self.name}, artist={self.artist}, year={self.year})"

    def __str__(self):
        return self.name


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    album_id = db.Column(db.Integer, db.ForeignKey("album.id"), nullable=False)
    album = db.relationship("Album", backref=db.backref("songs", lazy=True))

    @property
    def artist(self):
        return self.album.artist

    @property
    def year(self):
        return self.album.year

    def __repr__(self):
        return f"Song(name={self.name}, album={repr(self.album)})"

    def __str__(self):
        return self.name


class ArtistSchema(ma.ModelSchema):
    class Meta:
        model = Artist


class AlbumSchema(ma.ModelSchema):
    artist = fields.String()

    class Meta:
        model = Album


class SongSchema(ma.ModelSchema):
    year = fields.Integer()
    artist = fields.String()
    album = fields.String()

    class Meta:
        model = Song


# init schema
artist_schema = ArtistSchema(strict=True)
artists_schema = ArtistSchema(many=True, strict=True)

album_schema = AlbumSchema(strict=True)
albums_schema = AlbumSchema(many=True, strict=True)

song_schema = SongSchema(strict=True)
songs_schema = SongSchema(many=True, strict=True)
