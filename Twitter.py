
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
        self.Tweets.append(_addTweet)
        self.MyTweet.append(_addTweet)

    def Liked(self):
        for i in range(len(self.Tweets)):
            print(i, self.Tweets[i])
        indexTweet = input("Which Tweet Would You Like? ")
        self.Likes.append(self.Tweets[int(indexTweet)])

    def ListLikes(self):
        for tweet in self.Likes:
            print(tweet)

    def Retweet(self):
        for i in range(len(self.Tweets)):
            print(i, self.Tweets[i])
        indexTweet = input("Which Tweet Would You Like to Retweet? ")
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
        indexTweet = input("Which Tweet Would You Like to Un-Like? ")
        self.Likes.pop(int(indexTweet))


User1 =Twitter("Roaa")
print("         WELCOME To Twitter      ")
print("          | Time Line |      ")
User1.TimeLine()

UserOptions = ""
# User1.addTweet()
# User1.TimeLine()

#Using while looop
while UserOptions != "q" :
    print("1- To Add Tweet\n"+
            "2- To Like Tweet from Tweets\n"+
            "3- To Retweet from  Tweets\n"
            "4- To List all my liked tweets\n"
            "5- To List all my retweets\n"
            "6- To List all my tweets\n"
            "7- To Un-Like tweet from Likes\n"
            "8- To Un-Retweet from Retweets\n"
            "9- To Count my Tweets / Likes / Retweets\n"
            "10- To View Time Line Tweets")
            
    UserOptions=input("What Would You Like To Do? press the number to choose or 'q' to quit ")  
    if UserOptions == '1' :
        User1.addTweet()
    elif UserOptions == '2' :
        User1.Liked()
    elif UserOptions == '3' :
        User1.Retweet()
    elif UserOptions == '4' :
        User1.ListLikes()
    elif UserOptions == '5' :
        User1.ListRetweet()
    elif UserOptions == '6' :
        User1.MyTweets()
    elif UserOptions == '7' :
        User1.UnLikeTweets()
    elif UserOptions == '10' :
        User1.TimeLine()
    