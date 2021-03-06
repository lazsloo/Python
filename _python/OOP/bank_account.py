class BankAccount:
    def __init__(self, int_rate, balance):
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

bank_of_fail = BankAccount(0.01, 0)
bank_of_fail.deposit(200).deposit(150).deposit(50).withdraw(100).yield_interest().display_account_info()

bank_of_love = BankAccount(0.01, 0)
bank_of_love.deposit(1500).deposit(1500).withdraw(200).withdraw(150).withdraw(300).withdraw(50).yield_interest().display_account_info()