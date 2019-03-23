from . import db
from . import ma


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
        return f"{self.artist} - {self.name}"


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
        return f"{self.artist} - {self.name}"


class ArtistSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'bio')


# init schema
artist_schema = ArtistSchema(strict=True)
artists_schema = ArtistSchema(many=True, strict=True)
