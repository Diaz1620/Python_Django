from _typeshed import Self


class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    # adding deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self,amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.name + ", Balance: $" + str(self.account_balance) )
    def transfer(self, name, amount):
        self.make_withdrawal(amount)
        name.make_deposit(amount)
        self.display_user_balance()
        name.display_user_balance()

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(100).make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)
print(monty.account_balance)
guido.make_withdrawal(50).display_user_balance()


larry = User("Larry Larrod", "ll@test.com")
harry = User("Harry Potts", "harryp@wiz.com")

larry.make_deposit(100).make_deposit(300).make_deposit(200).display_user_balance().transfer(harry, 200)

