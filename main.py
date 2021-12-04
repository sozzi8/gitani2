
from lyrics import get_lyric
from checker import check
artist = "coldplay"
title= "the scientist"

song = get_lyric(artist, title)

print(title," by: ", artist)
print(song)
