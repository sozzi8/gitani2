"""
This is the main file where we created
the interaction between the user and the
database of guitarists and bands.
We use the argparse module to let the user
put the name of the song and the artist.

We also provide a functionality with textblob
in order to output the language of the song.

"""
from lyrics import get_lyric
from textblob import TextBlob
import csv_file
import argparse as ap

#pip install -U textblob
#python -m textblob.download_corpora

csv_path = 'reader.csv'




parser = ap.ArgumentParser(description = "the program " +
                                        "let you put the name "+
                                        "of an artist and his song "+
                                        "in order to retrieve the "+
                                        "correspondant lyric... "+
                                        "please wrap the argument "+
                                        "around quotes ")
parser.add_argument("artist", help="Please put the name of the artist", type= str)
parser.add_argument("title", help="Please put the name of a song of the artist", type= str)

args = parser.parse_args()
artist=args.artist
title=args.title

#lyric function to print the text of the selected song
song = get_lyric(artist, title)
print("{} by {}:".format(title, artist))
print("{}".format(song))
#we checked wether the lyric was in form of a string or not to see if the


#use textblob library and detect_language function to determine the language of the song
text1= artist + title
lan1= TextBlob(song)
print("the language of the song is:", lan1.detect_language())

parser.add_argument("-l", "--like", action="append", help="add a new song to playlist")
args = parser.parse_args()
like=args.like

if args.like:
    print("add to likes")

"""
return the lyric of the last song you searched for
"""
if __name__ == '__main__':
    csv_file. write_data(csv_path, args.artist, args.title, song)

#print(text1.translate(to = 'es'))
