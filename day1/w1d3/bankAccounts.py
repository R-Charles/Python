class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("insufficient funds")
            return self
        self.balance = self.balance - amount
        print(self.balance)
        return self

    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self


my_bankAccount = BankAccount(.6, 100)


my_bankAccount2 = BankAccount(.6, 100)
my_bankAccount.deposit(0).display_account_info().deposit(75).withdraw(125).deposit(20).yield_interest().display_account_info()

my_bankAccount2.deposit(0).display_account_info().deposit(75).withdraw(125).withdraw(20).withdraw(125).withdraw(85).yield_interest().display_account_info()
