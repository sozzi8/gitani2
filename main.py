from lyrics import get_lyric
from textblob import TextBlob
import argparse as ap

#pip install -U textblob
#python -m textblob.download_corpora

parser = ap.ArgumentParser() #argparse to insert title and artist's name
parser.add_argument("artist", help="First artist", type= str)
parser.add_argument("title", help="Song of the first artist", type= str)
args = parser.parse_args()
artist=args.artist
title=args.title

song = get_lyric(artist, title) #lyric function to print the text of the selected song

print("{} by {}:".format(title, artist))
print("{}".format(song))

#use textblob library and detect_language function to determine the language of the song
text1= artist + title
lan1= TextBlob(text1)
print("the language of the song is:", lan1.detect_language())
