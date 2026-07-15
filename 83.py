class BankAccout:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid amount")
    
    def get_balance(self):
        return self.__balance
    
    def get_owner(self):
        return self.__owner

user = BankAccout("John", 1000)
user.deposit(100)
user.withdraw(100)
print(user.get_balance())
print(user.get_owner())

print("program ended here")