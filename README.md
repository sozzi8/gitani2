
# IMPLEMENTATION OF AN API  OF LYRICS
Lyrics is a project that takes users' inputs from the machine terminal, checks whether or not they are written in the right format and then returns the lyric and the language of the requested song. Also, it creates a csv file with the last song that the user has searched, and with the optional argument ```-l "Yes" ``` , it adds to another csv the artist and the title of the song so that the user can have its own playlist.

## INSTALLATION
Use the command git clone https://github.com/sozzi8/gitani2.git  in the command prompt of your PC in order to automatically download the whole folder containing the modules. Git should have been previously installed on the machine. In alternative, just download manually the package from Github.

## USAGE
The aim of the project is to implement the functions of the [lyrics.ovh](https://lyricsovh.docs.apiary.io/#).
Once the two main arguments have been entered as input, the program will check if they are present inside the API, and if they are correctly written.
In case there are KeyError, the program will return an error message such as: ```ERROR: something went wrong!, Please try again```.
Whereas when the inputs are both present and correctly typed, the program will return the lyric of the requested song, its associated language, and a CSV file where the Last Song you searched for is stored.
Moreover,there is the possibility of specifying the optional argument ```-l "Yes" ``` , which lets you save the song in a playlist using a CSV file. 
Finally, in another CSV file are saved all the past researches.

If wanting to execute the program, the command should be written as follows:
  ```pyhton main.py "artist" "title"```
Where ```artist``` is the name of the singer and ```title``` is the name of the song. For example:
  ```python main.py "Vasco Rossi" "Vivere"```
In this case since the input is present and correct, the output will be the lyric of the song and its language

```Vivere by Vasco Rossi:
Vivere
è passato tanto tempo
Vivere!
è un ricordo senza tempo
Vivere
è un po' come perder tempo

Vivere.....e Sorridere!.......

VIVERE!

è passato tanto tempo

VIVERE!

è un ricordo senza tempo

VIVERE!

è un po' come perder tempo

VIVERE....e Sorridere dei guai

così come non hai fatto mai

e poi pensare che domani sarà sempre meglio

OGGI NON HO TEMPO

OGGI VOGLIO STARE SPENTO!



Vivere!

e sperare di star meglio

Vivere

e non essere mai contento

Vivere

come stare sempre al vento

VIVERE!......COME RIDERE!!!



VIVERE!

anche se sei morto dentro

VIVERE!

e devi essere sempre contento!

VIVERE!

è come un comandamento

VIVERE..... o SOPRAVVIVERE....

senza perdersi d'animo mai

e combattere e lottare contro tutto contro!.....

OGGI NON HO TEMPO

OGGI VOGLIO STARE SPENTO!.....



VIVERE

e sperare di star meglio

VIVERE VIVERE

e non essere mai contento

VIVERE VIVERE

e restare sempre al vento a

VIVERE.....e sorridere dei guai

proprio (così) come non hai fatto mai

e pensare che domani sarà sempre meglio!!!!!

the language of the song is: it
you haven't added this song to your playlist
```
To add the song to a playlist, the user can access a shortcut ```-l "Yes"``` thanks to ```[argparse]```. This command allows to add the ```Artist``` name and ``` Title ```of the song to the ```song.csv``` file and store a list of songs in order to create a playlist.


```Across the Universe by Beatles:
Words are flowing out like 
Endless rain into a paper cup
They slither wildly as they slip away across the universe.
Pools of sorrow waves of joy
Are drifting through my opened mind
Possessing and caressing me.

Jai Guru Deva. Om



Nothing's gonna change my world

Nothing's gonna change my world

Nothing's gonna change my world

Nothing's gonna change my world



Images of broken light, which 

Dance before me like a million eyes,

They call me on and on across the universe.

Thoughts meander like a 

Restless wind inside a letter box

They tumble blindly as they make their way across the universe.

Jai Guru Deva. Om



Nothing's gonna change my world

Nothing's gonna change my world

Nothing's gonna change my world

Nothing's gonna change my world



Sounds of laughter, shades of life

Are ringing through my opened ears 

Inciting and inviting me.

Limitless undying love, which

Shines around me like a million suns,

It calls me on and on across the universe

Jai Guru Deva, om.



Nothing's gonna change my world

Nothing's gonna change my world

Nothing's gonna change my world

Nothing's gonna change my world



Jai Guru Deva

Jai Guru Deva

Jai Guru Deva

Jai Guru Deva

Jai Guru Deva
you added a song to your playlist
{'Beatles': 'Across the Universe'}

the language of the song is: en
```

Whereas the songs.csv file is updated as follows: 

```
Across the Universe,Beatles
vivere,vasco rossi
```

Finally, using the command ``` python lastsong.py ```, the program returns the last song that the user searched for, and then adds it to the ```reader.csv``` file.


## CONTRIBUTING
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## LICENSE
[APACHE LICENSE, VERSION 2.0](https://www.apache.org/licenses/LICENSE-2.0)


Note that the project requires the ```json```, ```requests```, ```sys```, ```langdetect```, ```argparse```,```os```, ```unittest```, ```pandas``` and ``` csv```  modules to run.
