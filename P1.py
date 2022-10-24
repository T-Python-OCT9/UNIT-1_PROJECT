



import easy_

user_difclty = ['easy','normal', 'hard', 'very hard' ]

user = ''

go = 'go'

print('The game is very simple only you need to write the correct answer')


while user != go:
    user = input('Welcome to our game type go to play :  '  )

    if user == 'go':
        break
    else:
        print('please write go to play!')
    



    user_difclty = ['easy','normal', 'hard', 'very hard' ]

user_selction = input('please chose the difculty :\n 1-easy\n 2-normal\n 3-hard\n 4-very hard\n Exit to Exit the game\nPlease Choose :  ')
 
while user_selction == user_difclty[0]:

    easy_.easy()

if user_selction == user_difclty[1]:
    
    
    
    
    
    sol1, sol2, sol3, sol4, sol5, sol6, sol7, sol8 = 'Paris', 'Germany','Moscow','London','Rome','Madrid','Ukraine','Helsinki'
    user = ''
    exit = 'exit'
    number_of_gussung = 3
    hint = 'hint'
    number_of_hint = 2
    Score = 4
    user_name = input('Plese Enter Your Name to Start :  ')

    while user != sol1:

        user = input('Level [1] What is the capital of France? \n1-Paris \n2-Marseille \n3-Madrid \n: ')
        
        if sol1 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')

                exit()

                

    
                

            else:
                number_of_gussung-=1

           
        

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 2-Marseille')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            


        

    else:
        Score += 3
    
        print('True')

    while user != sol2:

        user = input ('Level [2] Berlin is the capital of which country? \n1-Finland \n2-Germany \n3-Italy \n: ')
        
        if sol2 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')

                exit()

                

            else:
                number_of_gussung-=1


        
            

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 3-Italy')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
        
        


    else:
        Score += 3
        
        print('True')

    while user != sol3:

        user = input ('Level [3] What is the capital of Russia? \n2-Saint Petersburg \n2-Moscow \n3-Kazan \n: ')
        
        if sol3 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1


            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()
            
                

            else:
                number_of_gussung-=1

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 3-Kazan')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            
 


    else:
        Score += 3
    
        print('True')


    while user != sol4:

        user = input ('Level [4] What is the capital of United Kingdom \n1-Birmingham \n2-Manchester \n3-London \n: ')
        
        if sol4 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or  user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()
                
             

            else:
                number_of_gussung-=1


        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 2-Manchester')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            



    else:
        Score += 3
    
        print('True')
   


    while user != sol5:

        user = input ('Level [5]What is the capital of Italy? \n1-Rome \n2-Milan \n3-Naples \n: ')
        
        if sol5 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()
               

            else:
                number_of_gussung-=1



        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 3-Naples')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            
            

        

    else:
        Score += 3

        print('True')

    while user != sol6:

        user = input ('Level [6] What is the capital of Spain? \n1-Madrid \n2-Barcelona \n3-Valencia \n: ')
        
        if sol6 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or user_name == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()
              

            else:
                number_of_gussung-=1


        

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 2-Barcelona')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
        

    

    else:
        Score += 3
        
        print('True')

    


    while user != sol7:

        user = input ('Level [7] Kiev is the capital of which country? \n1-Ukraine \n2-Kive Country \n3-Serbia \n: ')
        
        if sol7 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()

                
               

            else:
                number_of_gussung-=1


            

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 3-Serbia')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            


    else:
        Score += 3
       
        print('True')

    while user != sol8:

        user = input ('Level [8] What is the capital of Finland? \n1-Rovaniemi \n2-Helsinki \n3-Riyadh \n: ')
        
        if sol8 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1
           
            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()

          

            else:
                number_of_gussung-=1


            

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 1-Rovaniemi')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            
            

    else:
        Score += 3
        print('True')

if user_selction == user_difclty[2]:

     sol_1, sol_2, sol_3, sol_4, sol_5, sol_6, sol_7, sol_8 = 'Kabul', 'Jakarta','Beijing','Thailand','Islamabad','Tokyo','Viet Nam','Manila'
    
     user_name = input('Plese Enter Your Name to Start :  ')

     user = ''
     exit = 'exit'
     number_of_gussung = 3
     hint = 'hint'
     number_of_hint = 2
     Score = 4

     while user != sol_1:


        user = input('Level [1] What is the capital of Afghanistan \n1-Kandahar \n2-Kabul \n3-Kunduz \n: ')
        
        if sol_1 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')

                exit()

                

    
                

            else:
                number_of_gussung-=1

           
        

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 3-Kunduz')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            


        

     else:
        Score += 3
    
        print('True')

     while user != sol_2:

        user = input ('Level [2] What is the capital of Indonesia? \n1-Surabaya \n2-Medan \n3-Jakarta \n: ')
        
        if sol_2 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')

                exit()

                

            else:
                number_of_gussung-=1


        
            

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 1-Surabaya')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
        
        


     else:
        Score += 3
        
        print('True')

     while user != sol_3:

        user = input ('Level [3] -What is the capital of China? \n1-Hong Kong \n2-Beijing \n3-Tianjin \n: ')
        
        if sol_3 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1


            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()
            
                

            else:
                number_of_gussung-=1

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 1-Hong Kong')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            
 


     else:
        Score += 3
    
        print('True')


     while user != sol_4:

        user = input ('Level [4] Bangkok is the capital of which country? \n1-Thailand \n2-Pyongyang \n3-Seoul \n: ')
        
        if sol_4 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or  user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()
                
             

            else:
                number_of_gussung-=1


        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 2-Pyongyang')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            



     else:
        Score += 3
    
        print('True')
   


     while user != sol_5:

        user = input ('Level [5] What is the capital of Pakistan? \n1-Karachi \n2-Lahore \n3-Islamabad \n: ')
        
        if sol_5 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()
               

            else:
                number_of_gussung-=1



        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 1-Karachi')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            
            

        

     else:
        Score += 3

        print('True')

     while user != sol_6:

        user = input ('Level [6] What is the capital of Japan? \n1-Toyota \n2-Konan \n3-Tokyo \n: ')
        
        if sol_6 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or user_name == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()
              

            else:
                number_of_gussung-=1


        

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 2-Konan')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
        

    

     else:
        Score += 3
        
        print('True')

    


     while user != sol_7:

        user = input ('Level [7] Hanoi is the capital of which country? \n1-Tajikistan \n2-Korea  \n3-Viet Nam \n: ')
        
        if sol_7 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()

                
               

            else:
                number_of_gussung-=1


            

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 1-Tajikistan')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            


     else:
        Score += 3
       
        print('True')

     while user != sol_8:

        user = input ('Level [8] What is the capital of Philippines? \n1-Manila \n2-Las Pinas \n3-Makati \n: ')
        
        if sol_8 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1
           
            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()

          

            else:
                number_of_gussung-=1


            

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 2-Las Pinas')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            
            

     else:
        Score += 3
        print('True')

    
if user_selction == user_difclty[3]:

     sol_1, sol_2, sol_3, sol_4, sol_5, sol_6, sol_7, sol_8 = 'Abuja', 'Accra','Mali','Bangui','Cape Town','Dakar','Harare','Uganda'
    
     user_name = input('Plese Enter Your Name to Start :  ')

     user = ''
     exit = 'exit'
     number_of_gussung = 3
     hint = 'hint'
     number_of_hint = 2
     Score = 4

     while user != sol_1:


        user = input('Level [1] What is the capital of Nigeria? \n1-Kandahar \n2-Abuja \n3-Benin City \n: ')
        
        if sol_1 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')

                exit()

                

    
                

            else:
                number_of_gussung-=1

           
        

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 3-Benin City')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            


        

     else:
        Score += 3
    
        print('True')

     while user != sol_2:

        user = input ('Level [2] What is the capital of Ghana? \n1-Kumasi \n2-Tamale \n3-Accra \n: ')
        
        if sol_2 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')

                exit()

                

            else:
                number_of_gussung-=1


        
            

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 2-Tamale')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
        
        


     else:
        Score += 3
        
        print('True')

     while user != sol_3:

        user = input ('Level [3] Bamako is the capital of which country? \n1-Mali \n2-Ethiopia \n3-Algeria \n: ')
        
        if sol_3 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1


            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()
            
                

            else:
                number_of_gussung-=1

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 2-Ethiopia')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            
 


     else:
        Score += 3
    
        print('True')


     while user != sol_4:

        user = input ('Level [4] What is the capital of Central Africa? \n1-Mambere-Kadei \n2-Carnot \n3-Bangui \n: ')
        
        if sol_4 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or  user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()
                
             

            else:
                number_of_gussung-=1


        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 1-Mambere-Kadei')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            



     else:
        Score += 3
    
        print('True')
   


     while user != sol_5:

        user = input ('Level [5] What is the capital of South Africa? \n1-Alice \n2-Butterworth \n3-Cape Town \n: ')
        
        if sol_5 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()
               

            else:
                number_of_gussung-=1



        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 1-Alice')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            
            

        

     else:
        Score += 3

        print('True')

     while user != sol_6:

        user = input ('Level [6] What is the capital of Senegal? \n1-Dakar \n2-Diourbel \n3-Thies \n: ')
        
        if sol_6 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or user_name == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()
              

            else:
                number_of_gussung-=1


        

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 2-Diourbel')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
        

    

     else:
        Score += 3
        
        print('True')

    


     while user != sol_7:

        user = input ('Level [7] What is the capital of Zimbabwe? \n1-Mutare \n2-Bulawayo  \n3-Harare \n: ')
        
        if sol_7 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()

                
               

            else:
                number_of_gussung-=1


            

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 2-Bulawayo')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            


     else:
        Score += 3
       
        print('True')

     while user != sol_8:

        user = input ('Level [8] Kampala is the capital of which country? \n1-Uganda \n2-Rwanda \n3-Congo \n: ')
        
        if sol_8 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1
           
            if number_of_gussung == 0 or user == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                exit()

          

            else:
                number_of_gussung-=1


            

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 3-Congo')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            
            

     else:
        Score += 3
        print('True')





