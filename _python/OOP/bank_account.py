class BankAccount:
    def __init__(self, int_rate, balance):
        self.rate = int_rate
        self.bal = balance
    
    def deposit(self, amount):
        self.bal += amount
        return self

    def withdraw(self, amount):
        if self.bal >= amount:
            self.bal -= amount
        else:
            print("Insufficent funds: Charging $5 fee")
            self.bal -= 5
            self.bal -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.bal}")
        return self

    def yield_interest(self):

        return self

bank = BankAccount(0.01, 0)
bank.deposit(100).display_account_info()