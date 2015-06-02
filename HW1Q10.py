class BankAccount:

    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.num_fees = 0 

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 5
            self.num_fees += 5

    def get_balance(self):
        return self.balance

    def get_fees(self):
        return self.num_fees

def main():
    my_account = BankAccount(10)
    my_account.withdraw(5)
    my_account.deposit(10)
    my_account.withdraw(5)
    my_account.withdraw(15)
    my_account.deposit(20)
    my_account.withdraw(5) 
    my_account.deposit(10)
    my_account.deposit(20)
    my_account.withdraw(15)
    my_account.deposit(30)
    my_account.withdraw(10)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(50) 
    my_account.deposit(30)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(5) 
    my_account.deposit(20)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.deposit(30)
    my_account.withdraw(25) 
    my_account.withdraw(5)
    my_account.deposit(10)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(10) 
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.deposit(30)
    my_account.withdraw(25) 
    my_account.withdraw(10)
    my_account.deposit(20)
    my_account.deposit(10)
    my_account.withdraw(5) 
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(5) 
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(5) 
    print (my_account.get_balance(), my_account.get_fees())
main()
