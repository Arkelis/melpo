import glob
import eyed3
from melpo_api import db

LIBRARY_PATH = "/media/donnees/Musique/Artistes/4. Rock/Muse"

def scan():
    print("Launching files lookup.")
    for i, path in enumerate(glob.iglob(LIBRARY_PATH + "/**/*.mp3", recursive=True)):
        file = eyed3.load(path)
        try:
            print(file.tag.title)
            db.session.add("")
        except:
            print("No title to read.")
    print(f"{i+1} files found.")

if __name__ == "__main__":
    try:
        scan()
    except KeyboardInterrupt:
        print("\nExiting.")
        exit()
