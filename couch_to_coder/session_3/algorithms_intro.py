# A Simple programme to simulate
# a Bank ATM machine

#Initialize the variables
balance = 10000
pin = 2324
tries = 3


#Ask the user to input their pin
userPin = input("Enter your Pin: ")

while(tries > 0):
    
    #Check if user input is a valid digit
    if(not userPin.isdigit()):
        print("What you have entered above is not a valid digit")
        break

    #Check if user input is of a valid length
    if(len(userPin) != 4):
        break
    
    #Check if the user pin is correct
    if pin == int(userPin):
        userAction= input("Would you like to make a Withdrawal (W), Deposit (D) or see your account Balance (B) : ").lower()
        
        #Get user's preferred action and execute it
        if userAction == "w":
            amount = float(input("How much would you like to withdraw: ")) 
            balance = balance - amount
            print(f"Your updated account balance is £{balance}")
            break
        elif userAction == "d":
            amount = float(input("How much would you like to Deposit: ")) 
            balance = balance + amount
            print(f"Your updated account balance is £{balance}")
            break
        else:
            print(f"Your account balance is £{balance}")
            break

    else:
        tries -= 1
        #guard clause
        if(tries == 0):
            break
        userPin = (input("You have entered the wrong pin. Please try again : "))

    