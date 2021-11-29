from logging import error
import os
import eyed3
from sys import argv
import time

def main ():

    target_dir, artist = argv[1::]
    target_dir = validate_vals(target_dir)
    artist = validate_vals(artist)

    try:
        for song in os.listdir(target_dir):
            if ".mp3" in song:
                song = eyed3.load(target_dir + song)
                song.tag.artist = artist
                song.tag.album = artist
                song.tag.album_artist = artist

                song.tag.save()

    except:
        print("ERROR")

def validate_vals (value):
    if '"' in value:
        value = value.replace('"', '')
    
    return value


if __name__ == "__main__":
    if "--help" in argv or len(argv) != 3:
        print("Usage: \n>songs.py {target_dir} {artist_name} \nexample: >songs.py C:/Music/Manowar/ Manowar")
    else:
        main()