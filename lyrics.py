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
        if TypeError:
            print ("Error: not correclty typed")
            print ("TRY AGAIN")
            sys.exit()
#here with the except we stated that if the song is correctly written it can continue with the rest of the program, if there is a spelling error or maybe the song doesn't exists it arrests the rest of the code and gives a error messsage

    return song
