#Random app 
from InfoClass import *
from random import *

#a function that welcome the uesr
def user_suggestions():
   ''' this function will greet the user and show a list of suggestions to choose the kind of the shows they enjoy and it will show some random suggestion based on their taste on shows'''

   print("...."*3)

   #Categories sets start...
   categories = {"Action.","Kids.","Docuseries.","Drama.","Crimes.","Comedies."}

   action ={"The Batman","Demon Salyer","Memory","Jurassic World Dominion","Spider-Man: No Way Home","Doctor Strange in the Multiverse of Madness","Ambulance","Hunter X Hunter"}

   drama={"A silent Voice","Grave of the Fireflies","Parasite","A Beautiful Mind","The Good Doctor","Tomorrow"}
   
   comedies={"Reply 1988","The Office","Haikyuu","SPYx FAMILY","Gilmore Grils"}

   crimes={"Suits","Black List","Attack on titan","Voice","How to get away with Murder","Forgotten"}

   docuseries = {"Our Planet","Pandemic","The Great Hack","How To Chanage Your Mind","Mystery Lab"}

   kids = {"Cocomelon","Kung Fo Panda","Boss Baby","Dragon Legends","Badanamu Pop","Sponge Bob"}



   #Categories sets end...

   print (f"Here you can choose and write what kind of a series and movies you enjoy to watch:\n ")
   # for loop to print the list with numbers
   for index,categories in enumerate(categories):
    print('{}.{}'.format(index+1,categories))

   #massage for the user to enter the categories
   #if statment to check what the user decied and will show a list of shows based on what they choosed... 
   user_choosed = input("What you decied for today?\n")
   
   if user_choosed == "action":
      print(f"Here is some recommedation for action categories :\n")
      for index,action in enumerate(action):
       print('{}.{}'.format(index+1,action))  
   elif user_choosed == "drama":
      print(f"Here is some recommedation for drama categories :\n")
      for index,drama in enumerate(drama):
       print('{}.{}'.format(index+1,drama)) 
   elif user_choosed == "comedies":
      print(f"Here is some recommedation for comedies categories :\n")
      for index,comedies in enumerate(comedies):
       print('{}.{}'.format(index+1,comedies))
   elif user_choosed == "crimes":
      print(f"Here is some recommedation for crimes categories :\n")
      for index,crimes in enumerate(crimes):
       print('{}.{}'.format(index+1,crimes)) 
   elif user_choosed == "docuseries":
      print(f"Here is some recommedation for docuseries categories :\n")
      for index,docuseries in enumerate(docuseries):
       print('{}.{}'.format(index+1,docuseries))
   elif user_choosed == "kids":
      print(f"Here is some recommedation for kids categories :\n")
      for index,kids in enumerate(kids):
       print('{}.{}'.format(index+1,kids)) 

   user_show_info=input(" If you want to display the show summary please write the name of it : \n")
   # shows info imported from class shows
   #action shows info start...
   if user_show_info == "the batman":
      print(the_batman.ShowsInfo())

   elif user_show_info == "demon salyer":
      print(demon_salyer.ShowsInfo())

   elif user_show_info == "ambulance":
      print(Ambulance.ShowsInfo()) 

   elif user_show_info == "doctor strange":
      print(doctor_strange.ShowsInfo())

   elif user_show_info == "spider man":
      print(spider_man.ShowsInfo()) 

   elif user_show_info == "jurassic world":
      print(jurassic_world.ShowsInfo()) 

   elif user_show_info == "memory":
      print(memory.ShowsInfo())
   #action shows info end...
   #drama shows info start...
   elif user_show_info == "a silent voice":
      print(a_silent_voice.ShowsInfo()) 

   elif user_show_info == "tomorrow":
      print(tomorrow.ShowsInfo()) 

   elif user_show_info == "the good doctor":
      print(the_good_doctor.ShowsInfo())

   elif user_show_info == "a beautiful mind":
      print(a_beautiful_mind.ShowsInfo())   

   elif user_show_info == "parasite":
      print(parasite.ShowsInfo())

   elif user_show_info == "grave of the fireflies":
      print(grave_of_the_fireflies .ShowsInfo())                 
   #drama shows info end...
   #comedies shows info start...
   elif user_show_info == "gilmore grils":
      print(gilmore_grils.ShowsInfo()) 

   elif user_show_info == "spy x family":
      print(SPY_FAMILY.ShowsInfo()) 

   elif user_show_info == "haikyuu":
      print(Haikyuu.ShowsInfo())

   elif user_show_info == "the Office":
      print(the_Office.ShowsInfo())   

   elif user_show_info == "reply 1988":
      print(reply_1988.ShowsInfo())
                  
   #comedies shows info end...
   #crimes shows info start...
   elif user_show_info == "forgotten":
      print(forgotten.ShowsInfo()) 

   elif user_show_info == "How to get away with Murder":
      print(how_to_get_away.ShowsInfo()) 

   elif user_show_info == "voice":
      print(voice.ShowsInfo())

   elif user_show_info == "attack on titan":
      print(attack_on_titan.ShowsInfo())   

   elif user_show_info == "black list":
      print(black_list.ShowsInfo())
      
   elif user_show_info == "suits":
      print(suits .ShowsInfo())                 
   #crimes shows info end...
   #docuseries shows info start...
   elif user_show_info == "pandemic":
      print(pandemic.ShowsInfo()) 

   elif user_show_info == "our planet":
      print(our_Planet.ShowsInfo()) 

   elif user_show_info == "how to chanage your mind":
      print(How_To_Chanage_Your_Mind.ShowsInfo())

   elif user_show_info == "mystery_lab":
      print(Mystery_lab.ShowsInfo())   

   elif user_show_info == "the great hack":
      print(the_great_hack.ShowsInfo())
            
   #docuseries shows info end...
   #kids shows info start...
   elif user_show_info == "cocomelon":
      print(cocomelon.ShowsInfo()) 

   elif user_show_info == "kung fo panda":
      print(kung_fo_panda.ShowsInfo()) 

   elif user_show_info == "boss baby":
      print(boss_baby.ShowsInfo())

   elif user_show_info == "dragon legends":
      print(dragon_legends.ShowsInfo())   

   elif user_show_info == "badanamu pop":
      print(Badanamu_Pop.ShowsInfo())
      
   elif user_show_info == "sponge bob":
      print(sponge_bob.ShowsInfo())                 
   #kids shows info end...

def add_fav_list():
   '''ask the user to add to thier fav list or go back to the home page...'''  

   user_answer =input("Would you like to add a show to your favorite list? if Yes write\"y\"and \"c\" to check you favorite list,if you want to go back to the main page write \"back\":\n ")
   while True:
      if user_answer == "y":
         file = open("Fav_List.txt", "a", encoding="utf-8")
         user_fav_add = input("Please write what show you want to add to your favorite list : \n")
         file.write(user_fav_add + "\n")
         file.close
         user_add_another=input("would you like to add another favorite show?if Yes write\"y\"and \"c\" to check you favorite list,if you want to go back to the main page write \"back\":\n")
      elif user_answer =="c":
         file = open("Fav_List.txt","r", encoding="utf-8")
         file.seek(0)
         content=file.readlines()
         for index,FavList in enumerate(content):
            print(f"{index+1} - {FavList}")
         print(menu_list())
      elif user_answer or user_add_another =="back":
         print("see you next time!!")
         print(menu_list())
      break         

#Menu list for the program...
def menu_list()->str:
   '''This function will show a list and the user will type the number in the list to navigate through it '''
   print("\n")
   print("...."*3)
   print("\n")
   print("Hello there!, what is your mood to watch today?\n")
   Menu_items=("Browse the categories and ,get recommendations and summary for the show based on their type shows.\n ","Add and list your favorite shows.\n",)

   '''"Random options\n"'''
   
   for index,Menu_items in enumerate(Menu_items):
       print('{}.{}'.format(index+1,Menu_items)) 
   print("\n")    

   user_num_chosen=input("Please type the the number of list to navigate in the program: \n")
   
   #if statement to navigate through the program
   try:
      if user_num_chosen == '1':
         print(user_suggestions())
      elif user_num_chosen == '2':
         print(add_fav_list())
      return menu_list 
   except:
     print("An error occurred,please type only numbers to naviagte ")   
      
 
print(menu_list())
