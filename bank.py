import sys

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




if len(sys.argv)<2:
    print("❌ Error: Missing inputs.")
    print("Usage: python bank.py <action> <additional_arguments>")
    sys.exit()

action = sys.argv[1].lower()


if action == "create":
    if len(sys.argv)<3 : 
        print("❌ Error: Please provide data string in format Name-Balance")
        sys.exit()
    data_input = sys.argv[2]
    new_acct = BankAccount.create_from_string(data_input)
    print("🚀 New Account Created via Factory Method:")
    print(new_acct)

elif action == "currency":
    if len(sys.argv) < 2:
        print("❌ Error: Please provide a currency code (e.g., USD)") 
        sys.exit()
    currency_code = sys.argv[2]
    is_Supported = BankAccount.is_valid_currency(currency_code)
    if is_Supported:
        print(f"✅ Yes, {currency_code.upper()} is supported by our bank system.")
    else:
        print(f"❌ No, {currency_code.upper()} is NOT supported.")

elif action in ["deposit", "withdraw"]:
    if len (sys.argv) <3:
        print("❌ Error: Please specify an amount.")
        sys.exit()

    # Set up a default account to act on
    default_acct = BankAccount("Shreya", 1500.0)
        

    try:
        amount = float(sys.argv[2])
    except ValueError:
        print("❌ Error: Amount must be a clean number (e.g., 500), not words.")
        sys.exit()
    
    if action == "deposit":
        default_acct.deposit(amount) 
    elif action == "withdraw":
        default_acct.withdraw(amount)
    else:
        print(f"❌ Error: Unknown action '{action}'. Use 'deposit' or 'withdraw'.")

