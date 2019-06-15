# Melpo

Webapp lecteur de musique écrit en Flask (+Vue).

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

### Backend

```
$ cd backend
```

Il est conseillé d'utiliser [`poetry`](https://github.com/sdispater/poetry) pour gérer les
dépendances du projet. Le programme marche avec Python 3.7+. Pour installer les dépendances :

```
$ cd melpo/backend
$ poetry install
```

Grâce à `python-dotenv`, pas besoin de renseigner `FLASK_APP` et compagine, les options sont
indiquées dans `melpo/backend/.flaskenv`. Pour initialiser la base de donnée :

```
$ poetry run flask db upgrade
```

Pour lancer le backend :

```
$ poetry run flask run
```

### Frontend

```
$ cd webapp
```

En cours de développement.

## Feuille de route

* [ ] Backend
  * [x] Modèles
  * [x] API Artistes
  * [x] API Albums
  * [x] API Titres
  * [x] Scan des fichiers
* [ ] Frontend (App web)
* [ ] App mobile
* [ ] App desktop
