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
        if TypeError  in artist:
            print ("The artist name is mispelled ")
            sys.exit()
        elif TypeError(title):
            print("The title of the song is mispelled")
            sys.exit()
        else:
            print( "Error 404, check if you have correclty insert the name and the title")
            sys.exit()

    return song
