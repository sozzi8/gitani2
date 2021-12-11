import csv


def create_playlist(path):

    with open(path, 'w', newline='') as data:
        # create columns
        columns = ['artist', 'title']
        writer = csv.writer(data)
        writer.writerow(columns)
    return data


def write_data(path, artist, title):

    try:
        open(path)

    except:
        create_csv(path)

    m = [artist, title]

    with open(path, 'm', newline='') as data:

        rows = [line for line in csv.reader(data, delimiter=',')]

        if m not in rows:
            with open(path, 'a', newline='') as data:
                writer = csv.writer(data)
                writer.writerow(m)
