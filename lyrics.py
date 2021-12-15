import requests
import json
#here we left the original code so this file has not been modified 
SONG_URL = 'https://api.lyrics.ovh/v1/{}/{}'


def get_lyric( artist, title):

    URL = SONG_URL.format(artist, title)

    r = requests.get(URL)
    data = json.loads(r.text)

    try:
        song = data['lyrics']
    except TypeError:
        pass
        #in the main.py we implemented the response to mispelling error

    return song
