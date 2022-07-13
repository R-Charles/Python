from unicodedata import name


class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.03, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient funds!")
            return self
        self.balance = self.balance-amount
        print(self.balance)
        return self

    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self
        # self.balance = 100

    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self


my_bankAccount = BankAccount(0.03, 100)
my_bankAccount2 = BankAccount(0.03, 100)


my_bankAccount.display_account_info().withdraw(50).deposit(170).deposit(
    350).deposit(50).yield_interest().display_account_info()
my_bankAccount2.display_account_info().deposit(5).withdraw(50).deposit(
    200).withdraw(10).withdraw(60).withdraw(50).yield_interest().display_account_info()


class User():

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.01, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        # self.balance = self.balance + amount
        # print(self.balance)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self


Raphael = User('Raphael', 'Rapchar@gmail.com')
Raphael.make_deposit(500).make_withdraw(200).make_deposit(2000)
Raphael.display_user_balance()
