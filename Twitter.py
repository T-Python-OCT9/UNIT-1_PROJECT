
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

    #Time Line Method 
    def TimeLine(self):
        '''Method print all users tweets '''
        for tweet in self.Tweets:
            print("         " ,tweet)

    #AddTweet Method
    def addTweet(self):
        '''Method allow user to add a new tweet'''
        _addTweet = input("Add Your Tweet:🖌  ")
        if self.Validation(_addTweet):
            self.Tweets.append(_addTweet)
            self.MyTweet.append(_addTweet)

    #Liked Method
    def Liked(self):
        '''Method allows user to like any tweet in time line
            with validation tweet (check if already liked the tweet)'''
        for i in range(len(self.Tweets)):
            print(i, self.Tweets[i])
        indexTweet = input("\nWhich Tweet Would You Like? 'Note: You have to Type a number of tweet' 😎👍   ")
        if self.ValidationLike(self.Tweets[int(indexTweet)]):
            self.Likes.append(self.Tweets[int(indexTweet)])

    #ListLikes Method 
    def ListLikes(self):
        '''Method allows user to print all tweets that user liked it'''
        for tweet in self.Likes:
            print("         " ,tweet)

    #Retweets Method
    def Retweets(self):
        '''Method allows user to retweet any tweet'''
        for i in range(len(self.Tweets)):
            print("         ",i, self.Tweets[i])
        indexTweet = input("\nWhich Tweet Would You Like to Retweet? 'Note: You have to Type a number of tweet ' 😎🔁 ")
        if self.ValidationRetweet(self.Tweets[int(indexTweet)]):
            self.Retweet.append(self.Tweets[int(indexTweet)])

    #ListRetweet Method
    def ListRetweet(self):
        '''Method allows user to print all user's retweets '''
        for tweet in self.Retweet:
            print("         " ,tweet)

    #MyTweets Method
    def MyTweets(self):
        '''Method allows user to print all user tweets'''
        for tweet in self.MyTweet:
            print("         " ,tweet)

    #UnLikeTweets Method
    def UnLikeTweets(self):
        '''Method allows user to un-like tweet from liked tweets'''
        for i in range(len(self.Likes)):
            print("         ",i, self.Likes[i])
        indexTweet = input("\nWhich Tweet Would You Like to Un-Like? 'Note: You have to Type a number of tweet ' 🥲  ")
        self.Likes.pop(int(indexTweet))

    #UnRetweet Method
    def UnRetweet(self):
        '''Method allows user to retweet any tweet'''
        for i in range(len(self.Retweet)):
            print("         ",i, self.Retweet[i])
        indexTweet = input("\nWhich Tweet Would You Like to Un-Retweet? 'Note: You have to Type a number of tweet ' 🥲  ")
        self.Retweet.pop(int(indexTweet))

    #STATS Method
    def STATS(self):
        return " You have  -> {countTweet} Tweets  {countLikes}   Liked Tweets   {countRetweet}  Retweet ".format(countTweet = len(self.MyTweet) , countLikes=len(self.Likes) , countRetweet = len(self.Retweet))

    #Error handler to add a new Tweet  
    def Validation(self, Text : str):
        '''Method will check if your tweet has a value error'''
        if not (isinstance(Text , str) and len(Text) < 300) :
            raise ValueError("\n Tweet must be string and less than 300 characters 😓 \n")
        else:
            return True

    #Error handler to Retweet 
    def ValidationRetweet(self, Text : str):
        '''Method will check if you have already retweet it '''
        if Text in self.Retweet :
            raise ValueError("\n Sorry, You have already retweeted it 🥲🔁 \n")
        else:
            return True

    #Error handler to Like 
    def ValidationLike(self, Text : str ):
        '''Method will check if you have already Liked it '''
        if Text in self.Likes :
            raise ValueError("\n Sorry, You have already liked it 🥲  \n")
        else:
            return True

    #StartTwitter Method
    def StartTwitter(self):
        '''Method to start run twitter app'''
        print("      🥳️ WELCOME To Twitter 🥳️      ")
        print("          ⤹ Time Line ⤵      ")
        UserOptions = ""

        TimeLineCount =  lambda  : len(self.Tweets)
        print("     Current Tweets in Time Line ⇨ " , TimeLineCount() , " 👀")
        print("     Lets choose a number from the list 🧐!  ")
        #Using while looop
        while UserOptions != "q" :
            print("     1➜ To Add Tweet\n"
                    "     2➜ To Like Tweet from Tweets\n"
                    "     3➜ To Retweet from  Tweets\n"
                    "     4➜ To List all my liked tweets\n"
                    "     5➜ To List all my retweets\n"
                    "     6➜ To List all my tweets\n"
                    "     7➜ To Un-Like tweet from Likes\n"
                    "     8➜ To Un-Retweet from Retweets\n"
                    "     9➜ To Count my Tweets / Likes / Retweets\n"
                    "     10➜ To View Time Line Tweets \n")
                    
            UserOptions=input("What Would You Like To Do? press the number to choose or 'q' to quit ➜ ")  
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
                print(self.STATS())
            elif UserOptions == '10' :
                self.TimeLine()
