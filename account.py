from datetime import datetime


class Account:
    def __init__(self,accname,accnumber):
        self.accname = accname
        self.accnumber = accnumber
        self.balance = 0
        self.deposits =[]
        self.withdrawals =[]
        self.date =datetime.now().strftime("%x %X")
        self.transactions=100
        self.total = []
        self.loan_balance= 0

        


    def deposit(self,amount):
        deposits = {'date':self.date,'amount':amount,'naration':"deposits"}
        self.total.append(deposits)
        print (deposits)
        print (self.total)

        if amount <= 0:
            return f'Deposit must be positive amount'
        else:
            self.balance+=amount
            self.deposits.append(amount)
            print(self.deposits)
        return f'Hello {self.accname} you have deposited {amount} and your new balance is {self.balance} and your deposits are {self.deposits}'

    def withdraw(self,amount):
       withdrawals = {'date':self.date,'amount':amount,'narration':"deposits"}
       self.total.append(withdrawals)
       print (withdrawals)
       print (self.total)

       self.transactions = 100
       if amount <=0:
            return f'Withdraw should be positive'
       elif amount > self.loan_balance:
            return f'your balance is {self.balance} and you cannot withdraw {amount} '
       elif amount <=amount+self.transactions:
            return f'Hello {self.accname} you cannot  withdraw {self.transactions}'
       else:
            self.loan_balance -= amount+self.transactions
            self.withdrawals.append(amount)
            return f'Hello {self.accname} you have withdrawn {amount} and your new balance is {self.balance} , the transaction is {self.transactions} and your new withdrawal is {self.withdrawals}'

    def deposits_statement(self):
         for deposit in  self.deposits:
           print(deposit)

    def withdrawals_statement(self):
         for withdrawal in  self.withdrawals:
           print(withdrawal) 

    def current_balance(self):
        return f'{self.balance}'   

    def full_statement(self):
         statement=self.deposits+self.withdrawals
         for full in statement:
            print(full["narration"]) 

    def borrow(self):
        sum=0
        for borrowing in self.deposits:
            sum+=borrowing["amount"]
            
        if len(self.deposits) <10:
            return f"Hello {self.accname}  you are not qualified to borrow.make {10-len(self.deposits)} to borrow "
        if self.amount<100:
            return f"Hello {self.accname} you are qualified to borrow a loan"  
        if self.amount>sum/3:
            return f"Hello {self.accname} you can only borrow upto {sum/3}" 
        if self.loan_balance!=0:
            return f"Hello  {self.accname} you have {self.balance} you can't borrow any loan and you have a debt loan"
        if self.loan_balance!=0:
            return f"Hello you have a debt of {self.loan_balance} you have to pay first for you to borrow."
        else:
            interest= 3/100*(self.amount)
            self.loan_balance+=self.amount+interest
            return f"Hello {self.accname} you have borrowed {self.amount} your loan is now at {self.loan_balance}"
        
    


    def repayment_loan(self,amount):
        
         if amount>self.loan:
             self.balance+=amount-self.loan
             self.loan=0
             return f" Hello {self.accname}  thank you for paying the loan of {amount-self.loan} your account balance is {self.balance}"      
         else:
             self.loan-=amount
             return f"Hello {self.accname} you are appreciated for repayment of your loan"
    

    def transfer(self,amount,new_account):
        if amount<=0:
            return "invalid amount"
        if amount>=self.balance:
            return f"Hello {self.accname} you have insuficient amounts to do  transfer"
        if instance(new_account,Account):
            self.balance-=amount
            new_account.balance+=amount
            return f"you have sent {amount} to {new_account} with the name {new_account.name} and your new balance is {self.balance}"