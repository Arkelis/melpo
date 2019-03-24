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

Grâce à `python-dotenv`, pas besoin de renseigner `FLASK_APP` et compagine, les options sont
indiquées dans `backend/.flaskenv`. Pour initialiser la base de donnée :

```
$ cd backend
$ flask db upgrade
```

Pour lancer le site :

```
$ flask run
```
