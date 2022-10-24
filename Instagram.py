class Instagram:
    def __init__(self, userName : str ): 
        self.userName=userName       
        self.Posts = ["Python_Post","Lab_Post","Unit_Post","Python12_Post"]

        #Comment List:التعليقات
        self.Comment = ["Post","Post","Post"]
        #Likes List:-التفضيلات
        self.Likes = []
        #MyPost List:--------------
        self.Mypost = []
        #MyComment List:-----------
        self.Mycomment = []
    #_____________________________
    def TimeLine(self):
        for post in self.Posts:
            print(post)
    #______________________________
    def addPost(self):
        _addPost = input("Add Your Post: ")
        self.Posts.append(_addPost)
        self.Mypost.append(_addPost)

    #_____________________________________________________________
    def addComment(self):
        _addcomment = input("Add Your Comment: ")
        self.Comment.append(_addcomment)
        self.Mycomment.append(_addcomment)

    #______________________________________________________________
    def Liked(self):
        for i in range(len(self.Posts)):
            print(i, self.Posts[i])
        indexPost = input("Which Post Would You Like? ")
        self.Likes.append(self.Posts[int(indexPost)])
        
    #__________________________________________________________________
    def ListLikes(self):
        for post in self.Likes:
            print(post)

    #__________________________________________________________________
    def MyPost(self):
        for post in self.Posts:
            print(post)

    #_________________________________________________________________
   
    def ListComment(self):
        for post in self.Comment:
            print(post)
    #__________________________________________________________________

    def startInstagram(self):
         #User1 =Instagram("Najd")
        print("********************************** ")
        print("         WELCOME TO INSTAGRAM      ")
        print("                                    ")
        print("*********************************** ")
        print("                                    ")
        print("   Choose What You Want   ")
        print("                                    ")
        print("*********************************** ")
        UserOptions = ""
        ##############################################
        #Using while loop
        while UserOptions != "e" :
            print("     a) To Add Post\n"+"     b) To Like Post from Posts\n"+"     c) To Add Comment\n""     d) To List all my liked posts\n" "     f) To List all my comment\n"
                    "     g) To List all my posts\n" "     k) To View Time Line Posts \n")
        ##UserOptions ################   
            UserOptions=input("What Would You Like To Do? press the number to choose or 'e' to exit ")  
            if UserOptions == 'a' :
                self.addPost()
            elif UserOptions == 'b' :
                self.Liked()
            elif UserOptions == 'c' :
                self.addComment()
            elif UserOptions == 'd' :
                self.ListLikes()
            elif UserOptions == 'f' :
                self.ListComment()
            elif UserOptions == 'g' :
                self.MyPost()
            elif UserOptions == 'k' :
                self.TimeLine()
        else:
          print("Thank you for using the Instagram program, Come back again soon")
          ###########################
def Start():
    User =Instagram("Najd")
    try:
        User.startInstagram()
    except ValueError as err:
        print(err)
        #To Rerun the program
        Start()
    except IndexError as err1:
        print(err1)
        Start()
Start()