"""This is Melpo, version 0.0.1 main module file."""

from backend import app

if __name__ == '__main__':
    DEBUG = True
    app.run(port=8000)
