from Banks.Account import BankAccount
from Banks.Account import stupid
class User:
    # account
    def __init__(self, name):
        self.name = name
        self.accounts = {
            "Savings": BankAccount()
        }

    def main_account(self):
        return self.accounts["Savings"]
    
    def add_account(self, name, initial=0):
        self.accounts[name] = BankAccount(initial)

    def display_info(self):
        print(f"Name: {self.name}")
        # display all account balances
        for account in self.accounts:
            print(f"{account}: {self.accounts[account].balance}")

    def give_money(self, amount, target, account_type="Savings"):
        # target is a User
        # check to see if we have the funds
        if account_type in self.accounts and account_type in target.accounts:
            if self.accounts[account_type].make_withdraw(amount):
                target.accounts[account_type].make_deposit(amount)
        else:
            print(f"{account_type} not found in both users!")
    
    def total_funds(self):
        # all of the monies from all the accounts!
        # iterate dictionary
        # sum each key's account balance
        curr_balance = 0
        for acct_type, acct in self.accounts.items():
            curr_balance += acct.balance
        return curr_balance


ricky = User("Ricky")
ricky.add_account("Checking", 100000)
dicky = User("Dicky")
dicky.add_account("Checking", 50)

ricky.main_account().make_deposit(100)
ricky.display_info()
ricky.give_money(200, dicky, "Checking")

ricky.display_info()
dicky.display_info()

print(ricky.total_funds())
print(stupid)