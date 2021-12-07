import argparse


def my_playlist():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l",'--like', help= "messaggio", type=str, default= "no", choices= ["si","no"])
    args = parser.parse_args()

    pref=args.like
        # Print "Hello" + the user input argument


    if pref== "si":
        mylist+= [title]
        print("you added a song to your playlist")
        print(mylist)

my_playlist()
