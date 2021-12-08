import requests
import json
import sys
SONG_URL = 'https://api.lyrics.ovh/v1/{}/{}'


def get_lyric( artist, title):

    URL = SONG_URL.format(artist, title)

    r = requests.get(URL)
    data = json.loads(r.text)
    try:
        song = data['lyrics']
    except:
        if TypeError (artist):
            print ("The artist name is mispelled ")
            sys.exit()
        elif TypeError(title):
            print("The title of the song is mispelled")
            sys.exit()
        else:
            print( "riprova")
            sys.exit()

    return song
