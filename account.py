class Account:
    def __init__(self,accname,accnumber,balance):
        self.accname = accname
        self.accnumber = accnumber
        self.balance = balance


    def deposit(self,amount):
        self.balance+=amount
        return self.balance

    def withdraw(self,amount):
        self.balance-=amount
        return self.balance