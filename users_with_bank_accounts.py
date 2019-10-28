class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account.balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account.balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self

class BankAccount:
    def __init__(self, int_rate = 0.03, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee" )
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        self.balance *= 1 + self.int_rate
        return self

