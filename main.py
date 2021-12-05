from lyrics import get_lyric
from textblob import TextBlob
import argparse as ap

#pip install -U textblob
#python -m textblob.download_corpora

parser = ap.ArgumentParser()
parser.add_argument("artist", help="First artist", type= str)
parser.add_argument("song", help="Song of the first artist", type= str)
args = parser.parse_args()
artist=args.artist
song=args.song

song = get_lyric(artist, song)

print("{} by {}:".format(song, artist))
print("{}".format(song))


text1= artist + song
lan1= TextBlob(text1)
print("the language of the song is:", lan1.detect_language())
