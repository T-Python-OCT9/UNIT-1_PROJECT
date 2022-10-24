import re
def clear():
  string = open('orders.csv').read()
  new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
  open('c.txt', 'w').write(new_str)

clear()





def spilt ():
  new_set = set()
  with open('c.csv','r') as file:    
    for line in file:
	    for word in line.split():
             new_set.add(word)
  print(new_set)

def recommender(x:dict):
  if "Espresso" in cart:
    print("Do you want to add a cookie ? : ")
  
  elif "Macchiato" in cart:
    print("Do you want to add a chesecake ? : ")










  sys= {"Black", "Flat", "Espresso" , "Macchiato", "coppuccino", "Hot" , "Latte" , "Chicken" , "Nutella" ,"halloumi", "cheesecake" , "Cookie", "brownies" } 
#badchar = "{"



for character in file:
    if character.isalnum():
      remaining = file.read().replace(character, '')
      print (remaining)
#with open("orders.csv", mode = "w", errors='ignore') as newfile:
  #newfile.write(remaining)





'''def top(sys , new_set, word):
  for i in new_set:
    if i in sys :
        top_list = []
        top_list.append(word)
    else:
        continue

result= top(sys , new_set , word)
print (result)'''



#import pandas as pd

#df = pd.read_csv('orders.csv')
#df.head()

'''user_DB={}
def customer_data(name: str):
    i = 101
    for i in range(101 , 1001):
        user_DB.update(i , user_DB[name])
    print(user)
    file = open("orders.csv", "r", encoding="utf-8")
content = file.read()
file.close()'''


spilt()
