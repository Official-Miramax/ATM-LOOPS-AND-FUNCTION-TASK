# DATETIME MODULE 
# Register 
#- firstName, lastName, Email, UserPin, BVN
#- Generate Account Number

# LOGIN
#- Account Number & UserPin

# BANK OPERATIONS

# Importing Datetime from Datetime module
import time
from datetime import datetime

now = datetime.now()
dtString = now.strftime ("%d/%m/%y: %H:%M:%S %p")
print ("Date/Time =", dtString)

########### INITIALISING THE SYSTEM #########
import random

database = {}
saving_account_balance = (15000)
current_account_balance = (20000)

def init ():
    isValidOptionSelected = False
    print ("Welcome to Maxi Online Banking")

    while isValidOptionSelected == False:

        haveAccount = int ( input ("Do You Have an Account With Us?: \n1. (YES) \n2. (NO) \n"))

        if (haveAccount == 1):
            isValidOptionSelected = True 
            login ()
        
        elif(haveAccount == 2):
            isValidOptionSelected = True 
            register ()
        
        else:
            print ("Invalid Option Selected")

# USER LOGIN SECTION
def login ():

    print ("***** Login ***** \n")
    accountNumber = int (input ("Enter Account Number \n"))
    userPinLogin = int (input ("Enter User Pin \n"))

    for userAccountNumber, userDetails in database.items():
        if (accountNumber == userAccountNumber):
            if (userDetails[3] == userPinLogin):
                bankOperation()
            else:
                print ("Invalid username or Password \n")
                login ()
        
        else:
            print ("Invalid username or Password \n")
            login ()

# USER REGISTRATION SECTION
def register ():
    print ("******** Please Create An Account ******** \n")
    first_name = input ("What is your first name? \n")
    last_name = input ("What is your last name? \n")
    email = input ("What is your Email address? \n")
    userPin = int (input ("Create a 4 digit pin number? \n"))
    time.sleep(1.5)
    print ("Please wait, System is Processing..........")
    time.sleep(3.5)
    print ("Welcome %s, You have successfully created an account with us!!" %first_name)
    print ("====== ====== ====== ====== ====== ====== ======")

    userAccountNumber = generateUserAccountNumber ()

    #database[userAccountNumber] = [first_name, last_name, email, userPin]

    print ("Here is your Maxi Bank Account Number %d" % userAccountNumber)
    print ("====== ====== ====== ====== ====== ====== ======")
    print ("Make sure you keep it safe as it would be required to Login to your Account \n")

    database[userAccountNumber] = [first_name, last_name, email, userPin]
    login()

# USER BANKING OPERATION
def bankOperation():
    time.sleep(1.3)
    isValidOptionSelected = False
    while isValidOptionSelected == False:
        print ("Welcome, You are now logged in")
        selectedOption = int (input ("What would you like to do? \n 1. Withdrawal \n 2. Deposit \n 3. Check Balance \n 4. Complaints \n 5. Exit \n"))
        if (selectedOption == 1):
            isValidOptionSelected = True
            withdrawal()
        elif (selectedOption == 2):
            isValidOptionSelected = True
            deposit()
        elif (selectedOption == 3):
            isValidOptionSelected = True
            checkbalance()
        elif (selectedOption == 4):
            isValidOptionSelected = True
            complaint()
        elif (selectedOption == 5):
            isValidOptionSelected = True
            exit()

# DEFINNING THE WITHDRAWAL FUNCTION
def withdrawal():
    accountTypeSelection = int (input ("Select an Account Type \n1. Savings \n2. Current \n"))
    isValidOptionSelected = False 
    if (accountTypeSelection == 1):
        print ("1. 1000")
        print ("2. 3000")
        print ("3. 5000")
        print ("4. 10000")
        print ("5. other")
        optionSelect = int (input ("Please select an option \n"))
        isValidOptionSelected = True
        saving_account_balance
        if (optionSelect == 1):
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            time.sleep(3.5)
            print ("Your New Savings Account Balance: ", saving_account_balance - 1000)
            time.sleep(3.5)
            isValidOptionSelected = False
            while isValidOptionSelected == False:
                print ("\nWould you like To Do Something Else?")
                print ("1. YES")
                print ("2. NO")
                isValidOptionSelected = False
                while isValidOptionSelected == False:
                    alternateOption = int (input ("Please Select an Option\n"))
                    if (alternateOption == 1):
                        isValidOptionSelected = True
                        print ("1. Deposit")
                        print ("2. Complaint")
                        print ("3. Exit")
                        
                        altOptionSelect = int (input("Please Select an Option \n"))
                        if (altOptionSelect == 1):
                            isValidOptionSelected = True
                            withdrawal()
                
                        elif (altOptionSelect == 2):
                            isValidOptionSelected = True
                            complaints()

                        elif (altOptionSelect == 3):
                            isValidOptionSelected = True
                            exit()

                        else:
                            print ("Invalid Option Selected")

                    elif (alternateOption == 2):
                        isValidOptionSelected = True
                        exit()

                    else:
                        print ("Invalid Option Selected")





            
        elif (optionSelect == 2):
            saving_account_balance
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            print ("Your New Savings Account Balance: ", saving_account_balance - 3000)
        
        elif (optionSelect == 3):
            saving_account_balance
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            print ("Your New Savings Account Balance: ", saving_account_balance - 5000)

        elif (optionSelect == 4):
            saving_account_balance 
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            print ("Your New Savings Account Balance: ", saving_account_balance - 10000 )

        elif (optionSelect == 5):
            print ("How Much Would You Like To Withdraw?")
            amount = int (input ("Enter Amount \n"))
            saving_account_balance
            if amount < saving_account_balance:
                print ("Please Wait, Your Transaction is Processing......")
                print ("Take Your Cash.")
                print ("Your New Savings Account Balance: ", saving_account_balance - amount)

            else:
                print ("Insufficient Balance, Would you like to try something else?")
                print ("1. YES")
                print ("2. NO")

                option = int (input ("Please Select an Option \n"))
                if (option == 1):
                    bankOperation()

                elif (option == 2):
                    print ("Have a nice Day... \n")
                    login()
                    

    elif (accountTypeSelection == 2):
        print ("1. 1000")
        print ("2. 3000")
        print ("3. 5000")
        print ("4. 10000")
        print ("5. other")

        optionSelect = int (input ("Please select an option \n"))
        current_account_balance
        if (optionSelect == 1):
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            print ("Your New Current Account Balance: ", current_account_balance - 1000)
            

        elif (optionSelect == 2):
            current_account_balance
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            print ("Your New Current Account Balance: ", current_account_balance - 3000)
        
        elif (optionSelect == 3):
            current_account_balance
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            print ("Your New Current Account Balance: ", current_account_balance - 5000)

        elif (optionSelect == 4):
            current_account_balance 
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            print ("Your New Current Account Balance: ", current_account_balance - 10000)

        elif (optionSelect == 5):
            print ("How Much Would You Like To Withdraw?")
            amount = int (input ("Enter Amount \n"))
            current_account_balance
            if amount < current_account_balance:
                print ("Please Wait, Your Transaction is Processing......")
                print ("Take Your Cash.")
                print ("Your New Current Account Balance: ", current_account_balance - amount)

            else:
                print ("Insufficient Balance, Would you like to try something else?")
                print ("1. YES")
                print ("2. NO")

                option = int (input ("Please Select an Option \n"))
                if (option == 1):
                    bankOperation()

                elif (option == 2):
                    print ("Have a nice Day... \n")
                    login()

    else:
        print ("Invalid Option Selected")
        print(accountTypeSelection)


#DEFINNING THE DEPOSIT FUNCTION
def deposit():
    print ("Which account type would you like to deposit into?")
    print ("1. SAVINGS")
    print ("2. CURRENT")
    account_type_select = int (input ("Please Select an Option \n"))
    if (account_type_select == 1):
        print ("Your Savings Account Balance is", saving_account_balance)
        print ("How much would you like to deposit?")
        depositAmount = int (input ("Enter Amount \n"))
        saving_account_balance
        print ("Please Wait Your Transaction is Processing......")
        time.sleep(3.5)
        print ("Deposit Successful!!") 
        print ("Your New Savings Account Balance is: \n", saving_account_balance + depositAmount)
        print ("You deposited:", depositAmount)
        time.sleep(1.5)
        print ("\n **** CREDIT ALERT NOTIFICATION !!! ****")
        print ("Your savings Account Balance has Just been credited with", depositAmount)
        print ("Your New Savings Account Balance is:", saving_account_balance + depositAmount)
        time.sleep(1.5)
        print ("\n Would you like To Do Something Else?")
        print ("1. YES")
        print ("2. NO")
        

        alternateOption = int (input ("Please Select an  \n"))
        if (alternateOption == 1):
            print ("1. Withdraw")
            print ("2. Complaint")
            print ("3. Exit")
            altOptionSelect = int (input("Please Select an Option \n"))
            if (altOptionSelect == 1):
                withdrawal()
                
            elif (altOptionSelect == 2):
                complaints()

            else:
                print ("Invalid Option Selected")

        elif (alternateOption == 2):
            exit()

        else:
            print ("Invalid Option Selected")




def checkbalance():
    print ("some operations")

def complaints():
    user_complaint = input ("Please state your complaint and Press Enter \n")
    time.sleep(3.5)
    print ("Please wait, System is processing your complaint.....")
    time.sleep(2.5)
    print ("Your Complaint has been sent successfully, We would get back to you as soon as possible..")
    print ("Would you like to try something else? \n 1. YES \n 2. NO")


def exit():
    print ("Thanks for banking with us \nPlease Have a nice day !!")
    

def generateUserAccountNumber ():
    return random.randrange(1111111111,9999999999)
    generateUserAccountNumber ()


#print (generateUserAccountNumber())
init ()
