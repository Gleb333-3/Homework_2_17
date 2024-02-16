class bank:
    balance = 0
    def withdraw(self, amount):
        self.balance -= amount
        print(self.balance)
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)

account = bank()
account.deposit(12)
account.withdraw(4)
print(account.balance)