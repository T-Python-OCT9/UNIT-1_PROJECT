import random
'''

Made this seperate class to make the main looks more clean :D 

'''

class PersonalWallet():
    
    def main():
        print("*--- Hello and Welcome To Your Personal Wallet ! ---*\n")
        name_list, acc_num_list, acc_blc_list = PersonalWallet.read_file()
        option = 0
        while option != 6:

            print("  Please type in any of the below options to start !\n")
            # displaying option menu
            wallet_menu = ["*- 1. Open Account", "*- 2. Close Account", "*- 3. Withdraw Money",
                            "*- 4. Deposit Money", "*- 5. Logs Summary", "*- 6. Quit"]

            for option in wallet_menu:
                print(option)
            user_input = False

        # validation for user input
            while not user_input:
                try:
                    option = int(input("   Please type in an option number: "))
                    if 0 < option < 7:
                        user_input = True
                    else:
                        print("\nPlease enter a number greater than 0 and less than 7\n")
                        for option in wallet_menu:
                            print(option)
                except:
                    print("\nError -- Please enter a number between 1 to 6 only\n")
                    for option in wallet_menu:
                        print(option)


    # if statement for all of the options
            if option == 1:
                name_list, acc_num_list, acc_blc_list = PersonalWallet.open_acc(name_list, acc_num_list, acc_blc_list)

            elif option == 2:
                name_list, acc_num_list, acc_blc_list = PersonalWallet.close_account(name_list, acc_num_list, acc_blc_list)

            elif option == 3:
                name_list, acc_num_list, acc_blc_list = PersonalWallet.withdraw(name_list, acc_num_list, acc_blc_list)

            elif option == 4:
                name_list, acc_num_list, acc_blc_list = PersonalWallet.add_money(name_list, acc_num_list, acc_blc_list)

            elif option == 5:
                PersonalWallet.summary(name_list, acc_num_list, acc_blc_list)

            elif option == 6:
                PersonalWallet.exit(name_list, acc_num_list, acc_blc_list)


    # Functions for all of the switch statement
    def read_file():
        name_list = []
        acc_num_list = []
        acc_blc_list = []

    # reading the text file
        f = open("wallets_data.txt", "r", encoding="utf-8")
        lines = f.readlines()
        for line in lines:
            information = line.split()
            acc_num_list.append(information[0])
            acc_blc_list.append(float(information[1]))
            name_list.append(information[2])
        return name_list, acc_num_list, acc_blc_list


    # Function for opening an account
    def open_acc(name_list, acc_num_list, acc_blc_list):
        name = input("Please enter your name: ")
        print("Your name: ", name)
        name_list.append(name)
        # found = True
        # while found:
        number = str(random.randint(1, 9999))
        # check the number
        print("your account number: ", number)
        acc_num_list.append(number)

        initial_balance = float(input(f"Please Enter the Initial balance for {name}: "))
        acc_blc_list.append(initial_balance)

        print(f"-- An account has been opened ! \n- Account name: {name} \n- initial balance of {name} is : {initial_balance} \n- Account number is: {number}")

        return name_list, acc_num_list, acc_blc_list


    # Function for closing an account
    def close_account(name_list, acc_num_list, acc_blc_list):
        account_number = input("\nEnter your account number:\n")
        index = 0
        found = False
        for i in acc_num_list:
            if i == account_number:
                found = True
                break
            index = index + 1
        if found:
            print(f"\n --- Closing the account {name_list[index]} --- \n - Account number was: {acc_num_list[index]} \n - Total balance of account was: {acc_blc_list[index]} \n -- Sorry to see you go *{name_list[index]}* --\n")
            # deletes the 3 lists from their index position.
            del acc_num_list[index]
            del acc_blc_list[index]
            del name_list[index]

        else:
            print("\nError -- No account exists under the number you entered \n")
        return name_list, acc_num_list, acc_blc_list


    # Function for Withdrawing money from an account
    def withdraw(name_list, acc_num_list, acc_blc_list):
        account_number = input("\nEnter your account number:\n")
        index = 0
        found = False
        for i in acc_num_list:
            if i == account_number:
                found = True
                break
            index = index + 1
        if found:
            problem = True
            while problem:
                try:
                    withdraw_amount = float(input("Enter the amount you want to withdraw:"))
                    # The Amount is the new amount the customer has withdrawn
                    if withdraw_amount < 0:  # if not a positive int print message and ask for input again
                        print("ERROR -- input must be a positive integer, try again")
                        break
                    amount = acc_blc_list[index] - withdraw_amount
                    # if the amount is greater than or = 0 it will take the amount away from the balance list.
                    if amount > 0:
                        acc_blc_list[index] = acc_blc_list[index] - withdraw_amount
                        print(f"An amount of ${(withdraw_amount)} is removed from your account {account_number}")
                        print(f"Your current balance is $ {acc_blc_list[index]:,} ")
                        print("")
                        problem = False
                    else:
                        print("Unfortunately you don't have a sufficient funds",
                            name_list[index])
                        print("Your balance after your current transaction is ", "$",
                            format(acc_blc_list[index], ".2f"), sep="")
                        print("")
                        break
                finally:
                    return name_list, acc_num_list, acc_blc_list
        else:
            print("\n Sorry that account number does not exist \n")
            return name_list, acc_num_list, acc_blc_list


    # Function for depositing an amount to an account
    def add_money(name_list, acc_num_list, acc_blc_list):
        account_number = input("\nEnter your account number:\n")
        index = 0
        found = False
        for i in acc_num_list:
            if i == account_number:
                found = True
                break
            index = index + 1
        if found:
            problem = True
            while problem:
                try:
                    deposit_amount = float(input("Enter the amount you want to deposit:"))
                    # The Amount of customer chooses to deposit
                    if deposit_amount < 0:  # if not a positive int print message and ask for input again
                        print("ERROR -- input must be a positive integer, try again")
                        break
                    amount = acc_blc_list[index] + deposit_amount
                    # if the amount is greater than or = 0 it will added to the balance list.
                    if amount > 0:
                        acc_blc_list[index] = acc_blc_list[index] + deposit_amount
                        print(f"An amount of $ {deposit_amount} is added to your account {account_number}")
                        print(f"Your current balance is $ {acc_blc_list[index]:,} ")
                        print("")
                        problem = False
                    else:
                        print(f"Error -- Please enter a positive number {name_list[index]}")
                        print(f"Your balance after your current transaction is $ {acc_blc_list[index]}")
                        print("")
                        break
                finally:
                    return name_list, acc_num_list, acc_blc_list
        else:
            print("\n Sorry that account number does not exist \n")
            return name_list, acc_num_list, acc_blc_list


    # Function to display a report for all the accounts details
    def summary(name_list, acc_num_list, acc_blc_list):
        if len(name_list) > 0:
            for i in range(len(acc_num_list)):
                print(f"\nClient {name_list[i]} who's account number is {acc_num_list[i]} has $ {acc_blc_list[i]: ,}")
                total = sum(acc_blc_list)
            print(f"\nTotal amount of deposit in the system is: {total: ,}")
            largest_deposit = max(acc_blc_list)
            print(f"\nThe largest amount of deposit in the system is:  ${largest_deposit: ,}\n ")
        else:
            print("There is no account data !")

    def exit(name_list, acc_num_list, acc_blc_list):
        print("Thank You For Using The Personal Wallet program !")
        quit_file = open("wallets_data.txt", "w", encoding="utf-8")
        for i in range(len(acc_num_list)):
            save = acc_num_list[i] + " " + str(acc_blc_list[i]) + " " + name_list[i] + "\n"
            quit_file.write(save)
        quit_file.close()

