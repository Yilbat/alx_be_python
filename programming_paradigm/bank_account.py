class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
    
    def deposit(self,amount):
        self.account_balance =self.account_balance + amount
    
    def withdraw(self,amount):
        if self.account_balance >= amount:
            self.account_balance =self.account_balance - amount
        else:
            self.account_balance = self.account_balance
            return False
    def display_balance(self):
        print(f'${self.account_balance}')

    

# TG = BankAccount(20000)

# print(TG.display_balance())
# TG.deposit(2000)
# print(TG.display_balance())
# TG.withdraw(20000)
# print(TG.display_balance())

        