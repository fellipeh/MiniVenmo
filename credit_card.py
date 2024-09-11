class CreditCard:
    def __init__(self, number, limit):
        self.number = number
        self.limit = limit
        self.balance = limit

    def charge(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
