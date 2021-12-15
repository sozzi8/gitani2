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

from csv_playlist import database_of_songs 
#pip install langdetect

csv_path = 'reader.csv'
myplaylist={}

parser = ap.ArgumentParser(description = "the program " +
                                                "let you put the name "+
                                                "of an artist and his song "+
                                                "in order to retrieve the "+
                                                "correspondant lyric... "+
                                                "please wrap the argument "+
                                                "around quotes ")
parser.add_argument("artist", help="Please put the name of the artist", type= str)
parser.add_argument("title", help="Please put the name of a song of the artist", type= str)

parser.add_argument("-l",'--like', help= "type -l yes to add the song to your playlist", type=str, default= "no", choices= ["yes","no"])

args = parser.parse_args()
artist=args.artist
title=args.title
pref=args.like




#lyric function to print the text of the selected song

#by trying the song if the input is mispelled the software will respond with an error message
try:
    song = get_lyric(artist, title)
    print("{} by {}:".format(title, artist))
    print("{}".format(song))
except KeyError:
    print("ERROR: something went worng!")
    print("please try again!")
    sys.exit()
#we checked wether the lyric was in form of a string or not to see if the

"""given the args.like argparse, you can now decide whether you want
to add the song to your playlist or not"""

if pref== "yes":  #if you type " -l yes"
    myplaylist[artist] =title #it will add the song to your playlist
    print("you added a song to your playlist")
    print(myplaylist) #and then show it to you


else:
    print ("you haven't added this song to your playlist") #if you type nothing or " -l no", it won't add the song

database_of_songs(myplaylist)

#df= (create_playlist("songs.csv"))


#use detect language library to determine
#the language of the selected song
lang= detect(song)
print("the language of the song is:", lang)

"""
return the lyric of the last song you searched for
"""
if __name__ == '__main__':
    csv_file. write_data(csv_path, args.artist, args.title, song)




#print(text1.translate(to = 'es'))
