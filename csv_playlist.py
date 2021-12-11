import csv
from lyrics import get_lyric
import pandas as pd

playlist = []
def database_of_songs(dictionary, name_csv="songs.csv"):
    """
    the following function takes the elements present
    in the dictionary and places them into a csv file
    named guitarists.csv that we will use as our database.
    We will be able to add new bands and guitarists then.
    """


    for key, value in dictionary.items():
        playlist.append([key, value])
        df = pd.DataFrame(playlist, columns=["artist", "title"])

    df1.to_csv("songs.csv")

    return print("database created successfully ", "lista:", playlist )
    #df.append(playlist)




#database_of_songs(playlist)
