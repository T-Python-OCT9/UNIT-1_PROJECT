from MedicineModule import Medicine

main_loop = True 
while main_loop:
        
        print("--------------------Welcome!!--------------------")
        print("--------------------------------------------------")
        print("1- Adding medicine to the store")
        print("2- Display medicine in the store")
        print("3- Searching for medicine")
        print("4- Removing medicine from the store")
        print("5- Report")
        print("--------------------------------------------------")
        User_selection = input("Select the required option:-> ")
        print("--------------------------------------------------")
        

        if User_selection == '1':
            loop = True
            while loop:
                name = input("Enter the medicine name:-> ").strip()
                quantity = input("Enter the medicine quantity:-> ").strip()
                date = input("Enter the medicine expire date:-> ").strip()
                print("--------------------------------------------------")
                medicine_object = Medicine(name,quantity,date)
                medicine_object.add_medicine()
                print("Medicines are added to the store")
                print("--------------------------------------------------")
                input("Press Enter to continue...")
                break
                    
            
        elif User_selection == '2':
            print("--------------------------------")
            print("Display the medicines")
            try:
                medicine_object.display_medicine()
            except:
                print("Object not dected!!, try to add a Medicine...")

            print("--------------------------------")
            input("Press Enter to continue...")
            
        

        elif User_selection == '3':
            print("Searching for a specifed medicine based on the name")
            medicine_name = input('Enter the medicine name:-> ').strip()
            try:
                medicine_object.search_medicine(medicine_name=medicine_name)
            except:
                print("Object not dected!!, try to add a Medicine...")
        
        
        elif User_selection == '4':
            
            print("Deleteing a specifed medicine from the store")
            medicine_name = input('Enter the medicine name:-> ').strip()
            try:
                medicine_object.delete_medicine(medicine_name=medicine_name)
            except:
                print("Object not dected!!, try to add a Medicine...")
                
        
        elif User_selection == '5':
            
            total_quantity,medicine_quantity= medicine_object.statistic_medicine()
            print("--------------------------------")
            print(f"Medicine quantity: {medicine_quantity}")
            print("--------------------------------")
            print(f"Total medicine quantity: {total_quantity}")
            print("--------------------------------")
            input("Press Enter to continue...")