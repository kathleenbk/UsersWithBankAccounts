class BankAccount:
    bank_accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        
        BankAccount.bank_accounts.append(self)

        
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        
        return (self.balance)
    
    def yield_interest(self):
        self.balance = self.balance * self.int_rate
        return self

    @classmethod
    def print_all(cls):
        for account in cls.bank_accounts:
            print(f"Balance: {account.balance}")


class User:

    def __init__(self, name):
        self.name = name
        self.account = BankAccount(1.02,0)
        
    def make_deposit(self, amount):
        
        self.account.deposit(amount)
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.display_account_info()}")
    

Katie = User("Katie")

Katie.make_deposit(1000)
Katie.make_withdrawal(200)
Katie.display_user_balance()

Nick = User("Nick")

Nick.make_deposit(3000)
Nick.make_withdrawal(400)
Nick.display_user_balance()