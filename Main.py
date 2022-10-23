from Twitter import *
# Here we start our program
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