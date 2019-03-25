# Melpo

Webapp lecteur de musique écrit en Flask (+React).

## Dépendances Backend

Le backend est une API écrite en Python avec Flask. L'application est construite avec :

* [Flask-SQLAlchemy](https://github.com/pallets/flask-sqlalchemy) pour créer les modèles.
* [Flask-Marshallow](https://github.com/marshmallow-code/flask-marshmallow) et 
  [Marshmallow-SQLAlchemy](https://github.com/marshmallow-code/marshmallow-sqlalchemy) pour créer les serializers.
* [Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate) pour gérer les migrations de bases de données.

Autres dépendances :

* [Python-dotenv](https://github.com/theskumar/python-dotenv) pour utiliser les fichiers`.flaskenv` et `.env` avec la
  commande `flask`.

## Installation

Commencer par cloner le dépôt :

```
$ git clone git@github.com:Arkelis/melpo.git     # ssh
$ git clone https://github.com/Arkelis/melpo.git # https
```

Il est conseillé d'utiliser [`pipenv`](https://github.com/pypa/pipenv) pour gérer les
dépendances du projet. Le programme marche avec Python 3.7+. Pour installer les dépendances :

```
$ pipenv install
```

Grâce à `python-dotenv`, pas besoin de renseigner `FLASK_APP` et compagine, les options sont
indiquées dans `melpo/backend/.flaskenv`. Pour initialiser la base de donnée :

```
$ cd melpo/backend
$ flask db upgrade
```

Pour lancer le site :

```
$ flask run
```

## Roadmap

* [ ] Backend
  * [x] Modèles
  * [ ] API Artistes
  * [ ] API Albums
  * [ ] API Titres
  * [ ] Scan des fichiers
* [ ] Frontend
