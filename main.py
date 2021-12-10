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
from langdetect import detect
import csv_file
import argparse as ap
import sys

#pip install langdetect

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



#use detect language library to determine the language of the selected song
lang= detect(song)
print("the language of the song is:", lang)

#from playlist.py import my_playlist
#my_playlist()





"""
return the lyric of the last song you searched for
"""
if __name__ == '__main__':
    csv_file. write_data(csv_path, args.artist, args.title, song)

#print(text1.translate(to = 'es'))
