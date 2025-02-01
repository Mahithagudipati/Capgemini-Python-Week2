# •	2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods.
#  Implement logic to prevent overdraft.

class Bankaccount:
    def __init__(self,amount=0):
        self.amount=amount
    def deposit(self,Deposited_amount):
        self.Deposited_amount=Deposited_amount
        print(f"Enter the amount that you want to deposit : {self.Deposited_amount}")
        self.amount+=Deposited_amount
    def withdrawl(self,Withdraw_amount):
        self.Withdraw_amount=Withdraw_amount
        print(f"Enter the amouunt you want to withdraw : {self.Withdraw_amount}")
        self.amount-=Withdraw_amount
    
    def display_amount(self):
        print(f"The total amount is : {self.amount}")

b=Bankaccount()
n=1

while n!=0:
    print("Press the key to perform the operation : \n 1.Show balance  \n 2.Deposit amount  \n 3.Withdraw amount \n 4.Exit")
    n=int(input())
    if n==1:
        print(f"Your current balance is : { b.display_amount()}")
       
    elif n==2:
        dep=int(input(f"Enter the amount that you want to deposit : "))
        b.deposit(dep)
    elif n==3:
        wit=print(f"Enter the amount that you want to withdraw : ")
        b.withdrawl(wit)
    else:
        print("You have exited from the home page.")
        

