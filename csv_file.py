import csv


def create_csv(path):
    
    with open(path, 'w', newline='') as data:
        # create columns
        columns = ['artist', 'data', 'lyric']
        writer = csv.writer(data)
        writer.writerow(columns)
    return data


def write_data(path, artist, title, lyric):

    try:
        open(path)

    except:
        create_csv(path)

    r = [artist, title, lyric]

    with open(path, 'r', newline='') as data:

        rows = [line for line in csv.reader(data, delimiter=',')]

        if r not in rows:
            with open(path, 'a', newline='') as data:
                writer = csv.writer(data)
                writer.writerow(r)
