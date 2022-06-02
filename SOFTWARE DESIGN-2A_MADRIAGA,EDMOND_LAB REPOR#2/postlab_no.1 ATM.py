from curses import raw
from select import select
from bank import Bank, SavingsAccount
#Implimentation of ATM class
class ATM (object):
    '''This class represent terminal-based ATM transaction'''
       #Implemetation of __init__
    def __init__(sefl, bank):
        self._account = None
        self._bank = bank
        self._methods = {} # Jump table for commands
        self._methods["1"] = self._getBalance
        self._methods["2"] = self._deposit
        self._methods["3"] = self._withdraw
        self._methods["4"] = self._quit      
    #Implementation of run method
    def run(self):
        '''Logs in users and processes their accounts'''
        failureCount = 0
        #Iterate the loop
        while True:
            # Prompt user to enter name
            userName=raw_input("Enter Name: ")
            # Prompt user to enter PIN
            pin=raw_input("Enter PIN: ")
            # Load account
            self._account=self._bank.get(pin)
            # If account was not found
            # Print "Error, unrecognized PIN"
            if (self._account==None) :
                #Display statement
                print ("Error, unrecognized name")
                failureCount+=1
            elif(self._account.getName ()!=userName) :
                #Display statement
                print ("Error, unrecognzed name")
                failureCount+=1           
            else : 
                self._processAccount()
                if (failureCount>=3) :
                    #Display statement
                    print("Shutting down and calling the cops!")
                    return
