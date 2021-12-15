
In this repository you can find a file named ```lyrics.py``` that implements the ```get_lyric( artist, title)``` function. It queries the [lyrics.ovh](https://lyricsovh.docs.apiary.io/#) website to fetch the lyrics of a song ```title``` by the specified ```artist```.
If you run the program, executing the main file with: ```python main.py``` it will give you results similar to the following:

If you run the program but the two main arguments are wrongly typed you will receive an error message like: ```ERROR: something went wrong!, Please try again```


Note that the project requires the ```json```, ```requests```, ```sys```, ```langdetect```, ```argparse```,```os```, ```unittest```, ```pandas``` and ``` csv```  modules to run.
