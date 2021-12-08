import os
import eyed3
from sys import argv

def main ():

    if len(argv) == 3:
        target_dir, artist = argv[1::]
        target_dir = validate_vals(target_dir)
        artist = validate_vals(artist)
        album = artist
    elif len(argv) == 4:
        target_dir, artist, album = argv[1::]
        target_dir = validate_vals(target_dir)
        artist = validate_vals(artist)
        album = validate_vals(album)

    try:
        for song in os.listdir(target_dir):
            if ".mp3" in song:
                name = song.replace('.mp3', '')
                song = eyed3.load(target_dir + song)

                if song.tag.artist != artist or song.tag.album != artist or song.tag.album_artist != artist:
                    song.tag.artist = artist
                    song.tag.album = album
                    song.tag.album_artist = artist

                if song.tag.title != name:
                    song.tag.title = name

                song.tag.save()

    except:
        print("ERROR")

def validate_vals (value):
    if '"' in value:
        value = value.replace('"', '')
    
    return value


if __name__ == "__main__":
    if "--help" in argv or (len(argv) != 3 and len(argv) != 4):
        print("Tool for redacting metadata\n\nUsage: \n>songs.py {target_dir} {artist_name} {album_name} \n\nExample: \n>songs.py C:/Music/Manowar/ Manowar \"Kings of Metal\"")
    else:
        main()