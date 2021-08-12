

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(.02)
    # adding deposit method
    def make_deposit(self, amount):
        self.account.deposit(amount)
        self.display_user_balance()
        return self
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        self.display_user_balance()
        return self
    def display_user_balance(self):
        print(self.name + ", Balance: " + str(self.account.display_account_info()))
        return self
    def transfer(self, name, amount):
        self.make_withdrawal(amount)
        name.make_deposit(amount)
        self.display_user_balance()
        name.display_user_balance()
        return self

class BankAccount:
    def __init__(self, int_rate, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        else: 
            self.balance -= amount
        return self
    def display_account_info(self):
        
        return self.balance
    def yield_interest(self):
        if self.balance > 0:
            self.balance+= self.balance * self.int_rate
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(100)
monty.make_deposit(50)
guido.display_user_balance()
monty.display_user_balance()
guido.make_withdrawal(50)


larry = User("Larry Larrod", "ll@test.com")
harry = User("Harry Potts", "harryp@wiz.com")

larry.make_deposit(100).make_deposit(300).make_deposit(200).display_user_balance().transfer(harry, 200)

