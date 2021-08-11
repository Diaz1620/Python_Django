class BankAccount:
    def __init__(self, int_rate, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        else: 
            self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance ",self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance+= self.balance * self.int_rate
        return self

account1= BankAccount(.02, 200)
account2= BankAccount(.01, 100)

account1.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()
account2.deposit(200).deposit(500).withdraw(20).withdraw(15).withdraw(5).withdraw(10).yield_interest().display_account_info()