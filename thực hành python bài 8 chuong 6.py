class Bank:
    Account_type = "savings"
    location = "Guntur"
    def __init__(self, name,Account_Numner,balance):
        self.nam = name
        self.Account_Number = Account_Number
        self.balance= balance
        self.Account_type= Bank.Account_type
        self.location.Bank.location

    def __repr__(self):
        print("welcome to the SBI ATM Machine")
        print("------------------------------")
        account_pin = int(input("please enter your pin number"))
        if(account_pin == 123):
            Account(self)
        else:
            print("Pin Incorrect. please try again")
            Error(self)
        return' ' .join([self.name,self.Account_Number])
def Error (self):

    account_pin = int(input("Please enter your pi nuber "))
    if (account_pin == 123):
        Account(self)
    else:
        print("Pin Incorrect. Please try again")
        Error(self)
def Account(self):
    print("your Card Number is:XXXX XXXX XXXX 1337")
    print("world you like to deposit/Withdraw/check Balance?")
    print("""
1)      Balance
2)      Withdraw
3)      Deposit
4)      Quit

""")
    option= int
