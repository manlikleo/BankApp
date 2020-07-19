
import random

class BankAccount: #initializing Bank account class
    def __init__(self,id,balance = 0):
        self.id = id
        self.balance = balance

    def getId (self):
        return self.id

#this function take the amount you put in as a deposit
    def getDeposit( self,amount): #the balance was zero but when you deposit it increase
        self.balance += amount #by the amount you deposit


    def getWithdraw (self,amount):#it takes the amount you withdraw as an arguement
        self.balance -= amount # the balance decreases by the amount you withdraw


    def getBalance(self):
        return self.balance



def main() : #creating accounts 
    accounts = []
    for i in range (1000,9999):
        account = BankAccount(i,0)
        accounts.append(account)
        

        #Bank_Processes
    while True : 
        #reading id from user
        id = int(input(" \n Enter Account Pin: "))

        #loop till id is valid
        while id < 1000 or id > 9999:
            id = int(input("\n Invalid Pin.. Re-enter: "))

            
        #iterating over account session
        while True :

            # displaying account menu
            print("\n1 - view account Balance \t 2- withhdraw \t 3 - Deposit \t 4-exit")

            selection = int(input("\n Enter your selection:  ")) #reading selection

            for acc in accounts:
                if acc.getId() == id:
                    accountObj = acc
                    break

            if selection == 1: # showing bank account
                print(accountObj.getBalance())
                
            elif selection == 2: # reading amount
                amt = float(input("\n Enter amount to withdraw: "))
                ver_withdraw = input ("Is this the correct amount, Yes or No ? " + str(amt) + " ")
                    
                if ver_withdraw == "Yes":
                    print("verify withdraw")
                    
                else:
                    break 

                if amt < accountObj.getBalance(): # checking amount to bank account balance
                    accountObj.withdraw(amt) #calling withdraw method from class
                    print ("\n Updated Balance:" + str(accountObj.getBalance()) + "n")

                else: 
                    print("\n You're Balance is less than withdrawl amount:" + str(accountObj.getBalance()) + " n "  ) 
                    print("\n Please make a deposit.")

            elif selection == 3:
                amt = float(input("\n Enter amount to deposit: "))
                ver_deposit = input ("Is this the Correct amount ,Yes, or No ? " + str(amt) + " ")

                if ver_deposit == "Yes": # depositing method to the bank account 
                    accountObj.deposit(amt) #updated account balance

                    print ("\n Updated Balance:" + str(accountObj.getBalance()) + " n")
                    
                else:
                    break


            elif selection == 4:
                    print ('nTransaction is now complete.')
                    print("Transaction number:",random.randint(10000,100000))
                    print (" Thanks for choosing us as your bank")
                    exit()

            else:
                print("Invalid choice")
main()




                    


























