class BankAccount:
    def __init__(self, name, balance =0.0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return (f"---PASSBOOK STATEMENT---\n Acccount Holder: {self.name}\n Current Balance: {self.balance}\n--------------------------")
    
    def deposit(self, amt):
        if amt > 0:
            self.balance+=amt
        else:
            print("Enter amount should be +ve")
    
    def withdraw(self, amt):
        if 0< amt <= self.balance:
            self.balance-=amt
        else:
            print("Insufficient Balance")
    

    @staticmethod
    def is_valid_currency(cur):
        return cur.upper() in ["IND", "USD", "EUR"]

    @classmethod
    def create_from_string(cls,data_string):
        name,balance_str = data_string.split("-") 
        return cls(name, float(balance_str))         

# Creating a standard account
acct1 = BankAccount("Shreya", 1500.0)
# print(acct1)
    
acct1.deposit(500)
acct1.withdraw(200)
print(acct1)  # Balance: 1800
    
# Creating an account from a string
acct2 = BankAccount.create_from_string("Rahul-3000")
print(acct2)
    
# Static Method
print("Is USD supported?", BankAccount.is_valid_currency("USD"))

