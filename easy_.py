def easy():

    sol1, sol2, sol3, sol4, sol5, sol6, sol7, sol8, sol9 ,sol10 = 'Saudi Arabia', 'Sanaa','Doha','Muscat','Amman','Khartoum','Kuwait city','Beirut','Cairo','Manama'
    user = ''
    exit = 'exit'
    number_of_gussung = 3
    hint = 'hint'
    number_of_hint = 2
    Score = 3
    user_name = input('Plese Enter Your Name to Start :  ')

    while user != sol1:

        user = input ('Level [1] Riyadh is the capital of which country? \n1-Saudi Arabia \n2-Kuwait \n3-Sudan \n: ')
        
        if sol1 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or number_of_gussung == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                import P1

            else:
                number_of_gussung-=1

           
        

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 2-Kuwait')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            


        

    else:
        Score += 3
    
        print('True')

    while user != sol2:

        user = input ('Level [2] What is the capital of Yemen? \n1-Aden \n2-Dhamar \n3-Sanaa \n: ')
        
        if sol2 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or number_of_gussung == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                import P1

                

            else:
                number_of_gussung-=1


        
            

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 2-Dhamar')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
        
        


    else:
        Score += 3
        
        print('True')

    while user != sol3:

        user = input ('Level [3] What is the capital of Qatar? \n2-Al Rayyan \n2-Doha \n3-Al Wakra \n: ')
        
        if sol3 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1


            if number_of_gussung == 0 or number_of_gussung == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                import P1
                

            else:
                number_of_gussung-=1

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 2-Al Wakra')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            
 


    else:
        Score += 3
    
        print('True')


    while user != sol4:

        user = input ('Level [4] What is the capital of Oman? \n1-Salalh \n2-Muscat \n3-Saham \n: ')
        
        if sol4 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or number_of_gussung == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                
                import P1

            else:
                number_of_gussung-=1


        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 3-Saham')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            



    else:
        Score += 3
    
        print('True')
   


    while user != sol5:

        user = input ('Level [5]What is the capital of Jordan? \n1-Zarqa \n2-Amman \n3-Irbid \n: ')
        
        if sol5 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or number_of_gussung == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                import P1

            else:
                number_of_gussung-=1



        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 1-Zarqa ')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            
            

        

    else:
        Score += 3

        print('True')

    while user != sol6:

        user = input ('Level [6] What is the capital of Sudan? \n1-Omdurman \n2-El-Obeid \n3-Khartoum \n: ')
        
        if sol6 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or number_of_gussung == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                import P1

            else:
                number_of_gussung-=1


        

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 1-Omdurman')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
        

    

    else:
        Score += 3
        
        print('True')

    


    while user != sol7:

        user = input ('Level [7] What is the capital of Kuwait? \n1Kuwait city \n2-Al Jahra \n3-Abu Hulayfah \n: ')
        
        if sol7 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1

            if number_of_gussung == 0 or number_of_gussung == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')
                import P1

            else:
                number_of_gussung-=1


            

        if user == str(hint) and number_of_hint > 0:
            number_of_hint-= 1
            print('Not 2-Al Jahra')

        if user == str(hint) and number_of_hint == 0:
            print('You have no more hints')
            


    else:
        Score += 3
       
        print('True')

    while user != sol8:

        user = input ('Level [8] What is the capital of Lebanon? \n1-Beirut \n2-Tripoli \n3-Sidon \n: ')
        
        if sol8 != user and user != hint:
            print(f'You have ( {number_of_gussung} ) Chance left')
            Score+= -1
           
            if number_of_gussung == 0 or number_of_gussung == str(exit):
                print('You can not guess more')
                print(f'{user_name} Your Score is [{Score}] ! ')

                import P1

            else:
                number_of_gussung-=1