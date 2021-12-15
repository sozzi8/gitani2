"""
This is the main file where we create the interaction
with the user.
We use the argparse module to let the user
put the name of the song and the artist.

We provide a functionality that detect the language
of our lyrics with the librart langdetect.

We then put an optional argument in order to
let the user have the possibility to save it in
a playlist.
"""
from lyrics import get_lyric
from langdetect import detect
import csv_file
import argparse as ap
import sys
from csv_playlist import database_of_songs

csv_path = 'reader.csv'

parser = ap.ArgumentParser(description="the program" +
                           " let you put the name" +
                           "of an artist and his song " +
                           "in order to retrieve the" +
                           "correspondant lyric... " +
                           "please wrap the argument " +
                           "around quotes.")

parser.add_argument( "artist", help="Please put the name of the artist",
                    type=str)
parser.add_argument( "title",
                    help="Please put the name of a song of the artist",
                    type=str)
parser.add_argument( "-l", '--like',
                    help= "type -l yes to add the song to your playlist",
                    type=str,
                    default= "no",
                    choices= ["yes","no"])
args = parser.parse_args()
artist = args.artist
title = args.title
pref = args.like


"""
Lyric function to both print the text of the selected song
and send an error message in case of misspelling
"""


try:
    song = get_lyric(artist, title)
    print("{} by {}:".format(title, artist))
    print("{}".format(song))
except KeyError:
    print("ERROR: something went worng!")
    print("please try again!")
    sys.exit()


"""
Given the args.like argparse, you can now decide whether you want
to add the song to your playlist or not.
just add -l "yes" in the command line.
if you don't specify anything or type -l "no",
the song won't be added to the playlist
"""

if pref == "yes":
    database_of_songs(artist, title )
    print ("you have added this song to your playlist")
else:
    print ("you haven't added this song to your playlist")

"""
Use detect language library to determine
the language of the selected song
"""

lang=detect(song)
print("the language of the song is:", lang)

"""
Return the lyric of the last song you searched for
"""

if __name__ == '__main__':
    csv_file. write_data(csv_path, args.artist, args.title, song)
