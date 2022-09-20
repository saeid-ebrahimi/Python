

# Define class BankAccount
class BankAccount:
    bank = "Melat"
    # Initialize balance to 0
    def __init__(self, name, balance=0.0):
        self.log("Account created!")
        self.name = name
        self.balance = balance

    def get_balance(self):  # Getter for balance
        self.log("Balance checked at " + str(self.balance))
        return self.balance

    def set_balance(self, new_balance):  # Setter for balance
        self.log("Balance changed to " + str(new_balance))
        self.balance = new_balance

    def log(self, message):  # Logging method
        my_log = open("Log.txt", "a")
        print(message, file=my_log)
        my_log.close()


if __name__ == "__main__":
    myBankAccount = BankAccount("David Joyner")
    print(myBankAccount.bank)
    #myBankAccount.set_balance(20.0)
    #print(myBankAccount.get_balance())
