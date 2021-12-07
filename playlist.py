import argparse

def my_playlist():
    mylist = []
    parser = argparse.ArgumentParser()
    parser.add_argument('--like', help= "type title and artist's name", type=str, required=True)
    args = parser.parse_args()

    pref=args.like
    # Print "Hello" + the user input argument


    if args.like:
        mylist+= [pref]
        print("you added a song to your playlist")
        print(mylist)
    
my_playlist()
