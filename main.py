from fish import fish


def chouseList():

    print('1-add new fish')
    print('2-add member hunted fish')
    print('3-Hunter report')
    print('4-exit')




def addFish(fishList):
    name = input("enter fish name: ")
    deep = input("enter fish live in which deep by meter: ")
    weight = input("enter fish weight by Kg: ")
    quality = input("enter fish quality: ")
    price = input("enter fish price: ")

    newFish=fish(name,deep,weight,quality,price)
    print(newFish.fishReport())
    fishList.append(newFish)#add new fish to fishlist 
    print("Fish have been added thank you\n")
    return fishList #to save thelast change



#MHlist= member hunte list :
def addMH(MHList ,fishList):
    name = input("Enter member name: ")
    templist=[name]#newlist first print name 


    cont = True
    while (cont):
        try:
            i = 0
            while i < len(fishList):#>print fishlist 
                print(1 + i, "-", fishList[i].getName())
                i = i + 1
            print(i+1,"- to Stop")#i used while bec need to print output

            fishHunted = int(input("chose fish he hunt number: "))
            x=i+1
            if (1 <= fishHunted <= i):
                templist.append(fishList[fishHunted-1])
            elif fishHunted > x:
                print("there is no option like that, please try again")
        except ValueError:
            
            print("invalid input, please try again")
        else:
            if fishHunted == i+1:
                print("Thank you member and hunt have been added")
                break


    print("\n", name, "have hunt:")
    i=1
    while i<len(templist):
        print(i,"-",templist[i].getName())
        i=i+1

    print("\n")
    MHList.append(templist)#mhlist git app and print newlist 

    return MHList




def printReport(MHList):
    for x in range(len(MHList)):
        print("\n", MHList[x][0], "have Hunt:")
        i = 1
        while i < len(MHList[x]):
            print(i, "-", MHList[x][i].getName())
            i = i + 1

    print("\nThis is the list of all member and haunted\n")




if __name__ == '__main__':
    print('Welcome to the hunter application')
    fishList = []
    MHList = []
    fish1 = fish('napoleon', 22, 25, 'thebest', 1500)
    fish2 = fish('najl', 11, 36, 'good', 100)
    fishList.append(fish1)
    fishList.append(fish2)

    cont= True
    while (cont):
        try:
            chouseList()
            cho=int(input("chose option number: "))
            if(1<=cho<=4):
                if cho==1:
                    fishList=addFish(fishList)
                elif cho==2:
                    MHList=addMH(MHList,fishList)#edit [mhlist] sand to (addmh) git [mhlist] bec well save >take name and create tumplist 
                elif cho==3:
                    printReport(MHList)
            else:
                print("there is no option like that, please try again")
        except ValueError:
            cout=True
            print("invalid input, please try again")
        else:
            if cho==4:
                print("Thank you for using our app Goodbye")
                exit()
