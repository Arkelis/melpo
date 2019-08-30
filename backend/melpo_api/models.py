from . import db
from . import ma
from marshmallow import fields, post_load

# Relation artiste <-> morceau
songs_artists = db.Table(
    "songs_artists",
    db.Column("song_id", db.Integer, db.ForeignKey("song.id")),
    db.Column("artist_id", db.Integer, db.ForeignKey("artist.id")),
)

# Modèles
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    bio = db.Column(db.Text(200))
    picture = db.Column(db.String(2048))

    @property
    def picture_url(self):
        return f"http://localhost:8000/image/artist/{self.id}"

    def __repr__(self):
        return f"Artist(name={self.name}, bio={self.bio})"

    def __str__(self):
        return self.name


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    year = db.Column(db.Integer)
    cover = db.Column(db.String(2048))

    def __repr__(self):
        return f"Album(name={self.name}, artist={self.artist}, year={self.year})"

    def __str__(self):
        return self.name


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    album_id = db.Column(db.Integer, db.ForeignKey("album.id"), nullable=True)
    album = db.relationship("Album", backref=db.backref("songs", lazy=True))
    length = db.Column(db.Integer)
    artists = db.relationship("Artist", secondary=songs_artists, backref=db.backref("songs_artists", lazy="dynamic"))
    path = db.Column(db.String(512))
    track_number = db.Column(db.String(3))

    @property
    def album_artist(self):
        return self.album.artist

    @property
    def year(self):
        return self.album.year

    def __repr__(self):
        if not album:
            return str(self)
        return f"Song(name={self.title}, album={repr(self.album)})"

    def __str__(self):
        return self.name


class ArtistSchema(ma.ModelSchema):
    picture_url = fields.String()

    class Meta:
        model = Artist
        fields = ("id", "name", "bio", "picture_url", "songs_artists")


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
