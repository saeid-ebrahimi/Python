

class BankAccount:
    def __init__(self, name, balance=0.0):
        self.log("Account created!")
        self.name = name
        self.balance = balance

    def get_balance(self):
        self.log("Balance checked at " + str(self.balance))
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.log("+" + str(amount) + ": " + str(self.balance))

    def withdraw(self, amount):
        self.balance -= amount
        self.log("-" + str(amount) + ": " + str(self.balance))

    def log(self, message):
        print(message)


if __name__ == "__main__":
    myBankAccount = BankAccount("David Joyner")
    myBankAccount.deposit(20.0)
    print(myBankAccount.get_balance())
    myBankAccount.withdraw(10.0)
    print(myBankAccount.get_balance())
