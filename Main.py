from Twitter import *

def Start():
    User1 =Twitter("Roaa")

    try:
        User1.StartTwitter()
    except ValueError as e:
        print(e)
        #To Rerun the program
        Start()
    except IndexError as e:
        print(e)
        Start()

Start()