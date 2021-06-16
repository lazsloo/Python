class User:
    def __init__(self, users):
        self.name = users
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        print(f"{self.name}, deposited {amount}")

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        print(f"{self.name}, withdrew {amount}")

    def display_user_balance(self):
        print(f"{self.name}, balance is: {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


matt = User("Matt Damon")
matt.make_deposit(100)
matt.make_deposit(7234.11)
matt.make_deposit(233.12)
matt.make_withdrawl(3054.22)
matt.transfer_money("ben", 100)
matt.display_user_balance()

mark = User("Mark Walhberg")
mark.make_deposit(100.24)
mark.make_deposit(1314.12)
mark.make_withdrawl(123.99)
mark.make_withdrawl(73)
mark.display_user_balance()

ben = User("Ben Affleck")
ben.make_deposit(100)
ben.make_withdrawl(7.10)
ben.make_withdrawl(50)
ben.make_withdrawl(1000)
ben.display_user_balance()