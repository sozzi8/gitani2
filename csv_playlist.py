import csv
from lyrics import get_lyric
import pandas as pd


"""
the following function adds the artist and title
selected by the user to the song.csv file in order
to create the user's playlist
"""
def database_of_songs(artist, title, name_csv="songs.csv"):

    with open('songs.csv','a') as fd:
        fd.write(title + ","+ artist + "\n")
