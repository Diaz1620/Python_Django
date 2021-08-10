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
        print(f"{self.name}, Balance: {self.account_balance}")

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)
print(monty.account_balance)
guido.make_withdrawal(50)
guido.display_user_balance


