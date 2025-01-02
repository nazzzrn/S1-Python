class BankAccount:
    def __init__(self,account_name,account_number,account_type,balance):
        self.account_name=account_name
        self.account_number=account_number
        self.account_type=account_type
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        self.display()
    def withdraw(self,amount):
        if(self.balance<amount):
            print("Insufficiet balance")
        else:
            self.balance=self.balance-amount
            self.display()
    def display(self):
        print("Account name:",self.account_name)
        print("Account number:",self.account_number)
        print("Account type:",self.account_type)
        print("Account balance:",self.balance)
name=input("Enter the account holder's name:")
num=input("Enter the account number:")
tp=input("Enter the account type:")
bal=int(input("Enter the initial balance:"))
acc=BankAccount(name,num,tp,bal)
while 1:
    ch=int(input("Choose one operation:\n1.Deposit\n2.Withdraw\n3.Display\n"))
    if ch==1:
        am=int(input("Ener the amount:"))
        acc.deposit(am)
    elif ch==2:
        am=int(input("Enter the amount:"))
        acc.withdraw(am)
    elif ch==3:
        acc.display()
    else:
        print("Not a valid choice")


    