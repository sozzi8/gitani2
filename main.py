

#artist = "Beatles"
#title= "Across the Universe"

from textblob import TextBlob
b = TextBlob('song1')
b.detect_language()


import argparse as ap

parser = ap.ArgumentParser()
parser.add_argument("artist1", help="First artist", type= str)
parser.add_argument("song1", help="Song of the first artist", type= str)
args = parser.parse_args()
artist1=args.artist1
song1=args.song1
print ("the language of this song is",b.detect_language)
