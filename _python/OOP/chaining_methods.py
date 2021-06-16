class User:
    def __init__(self, users):
        self.name = users
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        print(f"{self.name}, deposited {amount}")
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        print(f"{self.name}, withdrew {amount}")
        return self

    def display_user_balance(self):
        print(f"{self.name}, balance is: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


matt = User("Matt Damon")
matt.make_deposit(100).make_deposit(7234.11).make_deposit(233.12).make_withdrawl(3054.22).display_user_balance()
# matt.transfer_money("ben", 100)

mark = User("Mark Walhberg")
mark.make_deposit(100.24).make_deposit(1314.12).make_withdrawl(123.99).make_withdrawl(73).display_user_balance()

ben = User("Ben Affleck")
ben.make_deposit(100).make_withdrawl(7.10).make_withdrawl(50).make_withdrawl(1000).display_user_balance()