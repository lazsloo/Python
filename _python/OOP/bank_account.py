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
        amount = int(self.rate * self.bal)
        self.bal = amount
        return self

bank_of_fail = BankAccount(0.01, 0)
bank_of_fail.deposit(200).deposit(150).deposit(50).withdraw(100).yield_interest().display_account_info()

bank_of_love = BankAccount(0.01, 0)
bank_of_love.deposit(1500).deposit(1500).withdraw(200).withdraw(150).withdraw(300).withdraw(50).yield_interest().display_account_info()