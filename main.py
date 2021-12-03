from lyrics import get_lyric

artist = "Beatles"
title= "Across the Universe"

song = get_lyric(artist, title)

print("{} by {}:".format(title, artist))
print("{}".format(song))
from textblob import TextBlob
b = TextBlob("get_lyric")
b.detect_language()
print ("The language of the song is ", b.detect_language())
