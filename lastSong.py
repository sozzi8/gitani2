"""
In this file we give the user  the possibility to recover the last lyric
of the song they searched and study different type of error.
"""
import pandas as pd


def read_data(path):
    '''This function read the latest request
    and if wrong input, print the type of error'''
    try:
        user_data = pd.read_csv(path, sep=',', header=0)
    except FileNotFoundError:
        print('The file does not exist')
        return

    except ValueError:
        print('File has a wrong encoding')
        return

    except UnicodeDecodeError:
        print('File has a wrong encoding')
        return

    print(user_data['lyric'].iloc[-1])
# otherwise add lyrics to data


if __name__ == '__main__':
    path = 'reader.csv'
    read_data(path)
