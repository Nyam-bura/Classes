class Account:
    def __init__(self,accname,accnumber):
        self.accname = accname
        self.accnumber = accnumber
        self.balance = 0
        self.deposits =[]
        self.withdrawals =[]
        


    def deposit(self,amount):
        if amount <= 0:
            return f'Deposit must be positive amount'
        else:
            self.balance+=amount
            self.deposits.append(amount)
            print(self.deposits)
        return f'Hello {self.accname} you have deposited {amount} and your new balance is {self.balance} and your deposits are {self.deposits}'

    def withdraw(self,amount):
        self.transactions = 100
        if amount <=0:
            return f'Withdraw should be positive'
        elif amount > self.balance:
            return f'your balance is {self.balance} and you cannot withdraw {amount} '
        else:
            self.balance -= amount+self.transactions
            self.withdrawals.append(amount)
            return f'Hello {self.accname} you have withdrawn {amount} and your new balance is {self.balance} , the transaction is {self.transactions} and your new withdrawal is {self.withdrawals}'

    def deposits_statement(self):
         for m in  self.deposits:
           print(m,end="\n")

    def withdrawals_statement(self):
         for n in  self.withdrawals:
           print(n,end="\n") 

    def current_balance(self):
        return f'{self.balance}'             

    
 


