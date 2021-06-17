class User:
    def __init__(self, users):
        self.name = users
        self.account = BankAccount(int_rate = 0.01, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        # print(f"{self.name}, balance is: {self.account}")
        return self

    # def transfer_money(self, other_user, amount):
    #     self.account -= amount
    #     other_user.account += amount

class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficent funds: Charging $5 fee")
            self.balance -= 5
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    # def yield_interest(self):
    #     self.balance = self.balance + self.balance * self.int_rate
    #     return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.int_rate)
        return self

matt = User("Matt Damon")

matt.make_deposit(100).make_deposit(400).make_withdrawl(10000).display_user_balance()