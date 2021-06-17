class User:
    def __init__(self, users):
        self.name = users
        self.account = BankAccount(int_rate = 0.02, balance = 0)

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

    def intrest(self):
        self.account.yield_interest()
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
        print(f"${amount} was deposited for ma beah money")
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"${amount} was withdrawn, don't spend it on drugs")
        else:
            print("Insufficent funds: Charging $5 fee")
            self.balance -= 5
            self.balance -= amount
        return self

    def display_account_info(self):
        if self.balance > 0:
            print(f"Your current balance is: ${self.balance}. Don't let the wifey see this")
        else:
            print(f"Bro you're ${self.balance} stop drinking beah at tha bah or mar will kills yah")
        return self

    # def yield_interest(self):
    #     self.balance = self.balance + self.balance * self.int_rate
    #     return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.int_rate)
            print(f"Your intrest rate is: {self.int_rate}. Smaht guy trying to retire. What? you think yous betteh than me?")
        return self

matt = User("Matt Damon")

matt.make_deposit(100).make_deposit(400).make_withdrawl(200).intrest().display_user_balance()