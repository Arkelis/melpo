"""This is Melpo, version 0.0.1 main module file."""

from melpo_api import app

if __name__ == '__main__':
    from melpo_api.scan import scan
    scan()
