class Bank:
    def __init__(self, money):
        self.balanc = money

    def balance(self):
        print(f'balance: {self.balanc}')

    def deposit(self, dep):
        self.balanc += dep
        print(f'deposit of {dep} successfully made. New balance: {self.balanc}')

    def withdraw(self, wit):
        if self.balanc < wit:
            print('insufficient funds!')
        
        else:
            self.balanc -= wit
            print(f'withdrawal of {wit} successfully made. New balance: {self.balanc}')


user = Bank(1000)

user.balance()
user.deposit(100)
user.balance()
user.withdraw(1200)
user.withdraw(1000)