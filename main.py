class BankAccount:
    bank = "Anor Bank"

    def __init__(self, owner, balance, card_type, password):
        self.owner = owner
        self.balance = balance
        self.card_type = card_type
        self.password = password

    def show_account(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")
        print(f"Card: {self.card_type}")

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money


a1 = BankAccount("Ali", 1000, "Visa", 1234)
a2 = BankAccount("Vali", 2000, "MasterCard", 5678)

a1.show_account()
a2.show_account()

a1.deposit(500)
a1.withdraw(200)

a2.deposit(300)
a2.withdraw(100)

a1.show_account()
a2.show_account()
