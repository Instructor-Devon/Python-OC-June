stupid = "LOL"
class BankAccount:
    # balance
    # interest rate
    def __init__(self, balance=0, interest_rate=.13):
        self.interest_rate = interest_rate
        self.balance = balance
    
    def make_deposit(self, amount):
        # what if negative?
        self.balance += abs(amount)
        return self

    # return boolean: True if successfull, False if not
    def make_withdraw(self, amount):
        # cant get more than you have!
        if (self.balance - amount) < 0:
            print("Insuffienct Funds!")
            return False
        self.balance -= amount
        return True
    def display_account_info(self):
        print(f"Avaliable Funds: {self.balance}")

    def yeild_interest(self):
        interest_gains = self.interest_rate * self.balance
        self.balance += interest_gains
    # methods: make_deposit, make_withdraw, display_account_info, yeild_interest
