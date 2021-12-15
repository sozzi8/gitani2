import csv
from lyrics import get_lyric
import pandas as pd

def database_of_songs(artist, title, name_csv="songs.csv"):
    """
    the following function takes the elements present
    in the dictionary and places them into a csv file
    named songs.csv that we will use as our playlist.
    """

    with open('songs.csv','a') as fd:
        fd.write(title + ","+ artist + "\n")
