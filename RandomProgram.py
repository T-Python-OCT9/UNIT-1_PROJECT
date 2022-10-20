#Random app 

#a function that welcome the uesr
def user_suggestions():
   ''' this function will greet the user and show a list of suggestions to choose the kind of the shows they enjoy and it will show some random suggestion based on their taste on shows'''
   
   print("...."*3)
   print("Hello there!, what is your mood to watch today?")
   print("...."*3)
   #Categories sets start...
   categories = {"Action.","Kids.","Docuseries.","Drama.","Crimes.","Comedies."}

   action ={"The Batman","Kimetsu no Yaiba: Mugen Ressha-hen","Memory","Jurassic World Dominion","Spider-Man: No Way Home","Doctor Strange in the Multiverse of Madness","Ambulance","Hunter X Hunter: Phantom Rouge"}

   drama={"A silent Voice","Grave of the Fireflies","Parasite","Joker","A Beautiful Mind","The Good Doctor","Tomorrow"}
   
   comedies={"Reply 1988","The Office","Haikyuu","Gintama","Friends","SPYx FAMILY","Gilmore Grils"}

   crimes={"Suits","Black List","Monster","Attack on titan","Death Note","Voice","How to get away with Murder","Forgotten"}

   docuseries = {"Seen","Our Planet","Pandemic","The Great Hack","SPY Craft","How Tp Chanage Your Mind","Mystery Lab"}
   kids = {"Cocomelon","Kung Fo Panda","Boss Baby","Dragon Legends","Badanamu Pop","Sponge Bob"}

   #Categories sets end...

   print("Here you can choose and write what kind of a series and movies you enjoy to watch:\n ")
   # for loop to print the list with numbers
   for index,categories in enumerate(categories):
    print('{}.{}'.format(index+1,categories))

   #massage for the user to enter the categories
   user_choosed = input("What you decied for today?\n")
   
   if user_choosed == "":
    pass
   print()
   

print(user_suggestions())
