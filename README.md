# Melpo

Webapp lecteur de musique écrit en Flask (+React). Voir le Pipfile pour les dépendances.

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

Pour initialiser la base de donnée :

```
$ cd backend
$ export FLASK_APP=app
$ flask db upgrade
```

Pour lancer le site :

```
$ export FLASK_ENV=development
$ flask run
```
