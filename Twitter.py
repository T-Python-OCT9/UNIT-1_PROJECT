
class Twitter:
    def __init__(self, userName : str ): 
        self.userName=userName
        #List Tweet:
        self.Tweets = [
                    "First Tweet",
                    "Second Tweet",
                    "Third Tweet",
                    "Fourth Tweet",
                    "Fifth Tweet"
            ]
        #Likes List:
        self.Likes = []

        #Retweet List:
        self.Retweet = []

        #MyTweet List:
        self.MyTweet = []

    def TimeLine(self):
        for tweet in self.Tweets:
            print(tweet)

    def addTweet(self):
        _addTweet = input("Add Your Tweet: ")
        if self.Validation(_addTweet):
            self.Tweets.append(_addTweet)
            self.MyTweet.append(_addTweet)

    def Liked(self):
        for i in range(len(self.Tweets)):
            print(i, self.Tweets[i])
        indexTweet = input("\nWhich Tweet Would You Like? ")
        if self.ValidationLike(self.Tweets[int(indexTweet)]):
            self.Likes.append(self.Tweets[int(indexTweet)])

    def ListLikes(self):
        for tweet in self.Likes:
            print(tweet)

    def Retweets(self):
        for i in range(len(self.Tweets)):
            print(i, self.Tweets[i])
        indexTweet = input("\nWhich Tweet Would You Like to Retweet? ")
        if self.ValidationRetweet(self.Tweets[int(indexTweet)]):
            self.Retweet.append(self.Tweets[int(indexTweet)])

    def ListRetweet(self):
        for tweet in self.Retweet:
            print(tweet)

    def MyTweets(self):
        for tweet in self.MyTweet:
            print(tweet)

    def UnLikeTweets(self):
        for i in range(len(self.Likes)):
            print(i, self.Likes[i])
        indexTweet = input("\nWhich Tweet Would You Like to Un-Like? ")
        self.Likes.pop(int(indexTweet))

    def UnRetweet(self):
        for i in range(len(self.Retweet)):
            print(i, self.Retweet[i])
        indexTweet = input("\nWhich Tweet Would You Like to Un-Retweet? ")
        self.Retweet.pop(int(indexTweet))

    def STATS(self):
        return len(self.MyTweet) + " Tweets " +  len(self.Likes) + " Liked Tweets " + len(self.Retweet) + " Retweet "

    #Error handler | 
    def Validation(self, Text : str):
        if not (isinstance(Text , str) and len(Text) < 300) :
            raise ValueError("\n Tweet must be string and less than 300 characters \n")
        else:
            return True

    def ValidationRetweet(self, Text : str):
        if Text in self.Retweet :
            raise ValueError("\n You have already retweeted it \n")
        else:
            return True

    def ValidationLike(self, Text : str ):
        if Text in self.Likes :
            raise ValueError("\n You have already liked it \n")
        else:
            return True

    def StartTwitter(self):

        print("         WELCOME To Twitter      ")
        print("          ⤹ Time Line ⤵      ")
        UserOptions = ""

        TimeLineCount =  lambda  : len(self.Tweets)
        print("     Current Tweets in Time Line ⇨ " , TimeLineCount())

        #Using while looop
        while UserOptions != "q" :
            print("     1- To Add Tweet\n"+
                    "     2- To Like Tweet from Tweets\n"+
                    "     3- To Retweet from  Tweets\n"
                    "     4- To List all my liked tweets\n"
                    "     5- To List all my retweets\n"
                    "     6- To List all my tweets\n"
                    "     7- To Un-Like tweet from Likes\n"
                    "     8- To Un-Retweet from Retweets\n"
                    "     9- To Count my Tweets / Likes / Retweets\n"
                    "     10- To View Time Line Tweets \n")
                    
            UserOptions=input("What Would You Like To Do? press the number to choose or 'q' to quit ")  
            if UserOptions == '1' :
                self.addTweet()
            elif UserOptions == '2' :
                self.Liked()
            elif UserOptions == '3' :
                self.Retweets()
            elif UserOptions == '4' :
                self.ListLikes()
            elif UserOptions == '5' :
                self.ListRetweet()
            elif UserOptions == '6' :
                self.MyTweets()
            elif UserOptions == '7' :
                self.UnLikeTweets()
            elif UserOptions == '8' :
                self.UnRetweet()
            elif UserOptions == '9' :
                self.STATS()
            elif UserOptions == '10' :
                self.TimeLine()
