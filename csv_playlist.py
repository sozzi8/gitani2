import csv
from lyrics import get_lyric
import pandas as pd


def database_of_songs(dictionary, name_csv="songs.csv"):
    """
    the following function takes the elements present
    in the dictionary and places them into a csv file
    named guitarists.csv that we will use as our database.
    We will be able to add new bands and guitarists then.
    """

    playlist = []
    for key, value in dictionary.items():
        playlist.append([key, value])
    df = pd.DataFrame(playlist, columns=["artist", "title"])
    df.to_csv(name_csv)
    return print("database created successfully ")


#database_of_songs(myplaylist)
