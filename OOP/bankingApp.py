

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.checkings = BankAccount(.02)
        self.savings = BankAccount(.05, 100)
    # adding deposit method
    def make_deposit(self, amount, account):
        if account == "checkings":
            self.checkings.deposit(amount)
            # self.display_user_balance("checkings")
        elif account == "savings":
            self.savings.deposit(amount)
            # self.display_user_balance("savings")
        return self
    def make_withdrawal(self,amount, account):
        if account == "checkings":
            self.checkings.withdraw(amount)
            # self.display_user_balance("checkings")
        elif account == "savings":
            self.savings.withdraw(amount)
            # self.display_user_balance("savings")
        return self
    def display_user_balance(self, account):
        if account == "checkings":
            print(self.name + ", Balance: " + str(self.checkings.display_account_info()))
        elif account == "savings":
            print(self.name + ", Balance: " + str(self.savings.display_account_info()))
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
        print(f"Balance: ${self.balance}")
        return self.balance
    def yield_interest(self):
        if self.balance > 0:
            self.balance+= self.balance * self.int_rate
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(100, 'checkings')
guido.checkings.display_account_info()
guido.savings.display_account_info()
# monty.make_deposit(50)
# guido.display_user_balance()
# monty.display_user_balance()
# guido.make_withdrawal(50)


# larry = User("Larry Larrod", "ll@test.com")
# harry = User("Harry Potts", "harryp@wiz.com")

# larry.make_deposit(100).make_deposit(300).make_deposit(200).display_user_balance().transfer(harry, 200)

