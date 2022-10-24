from Instagram import *

def Start():
    User1 =Instagram("Najd")

    try:
        User1.startInstagram()
    except ValueError as err:
        print(err)
        #To Rerun the program
        Start()
    except IndexError as err1:
        print(err1)
        Start()

Start()