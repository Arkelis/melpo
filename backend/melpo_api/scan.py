import glob
import taglib
from flask import jsonify
from melpo_api import db

LIBRARY_PATH = "/media/donnees/Musique/Artistes/"

__all__ = ["scan"]

def _extract_metadata(file: taglib.File, tag: str) -> str:
    tag_list = file.tags.get(tag.upper())
    if tag_list is None:
        return {
            "TITLE": "Sans titre",
            "DATE": "Année inconnue",
            "ALBUM": "Sans album",
        }.get(tag)
    if any(tag_list):
        return tag_list[0]
    

def scan() -> dict:
    print("Launching files lookup.")
    results = []
    for i, path in enumerate(glob.iglob(LIBRARY_PATH + "/**/*.mp3", recursive=True)):
        file = taglib.File(path)
        metadata = {
            "track_number": _extract_metadata(file, "tracknumber"),
            "title": _extract_metadata(file, "title"),
            "album": _extract_metadata(file, "album"),
            "length": file.length,
            "artist": _extract_metadata(file, "artist"),
            "year": _extract_metadata(file, "date"),
            "path": path
        }
        results.append(metadata)
    return results


if __name__ == "__main__":
    try:
        scan()
    except KeyboardInterrupt:
        print("\nExiting.")
        exit()
