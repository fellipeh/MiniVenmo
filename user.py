from credit_card import CreditCard

class User:
    __slots__ = ('username', 'balance', 'credit_card', 'friends', 'activity_feed')

    def __init__(self, username, balance=0):
        self.username = username
        self.balance = balance
        self.credit_card = None
        self.friends = set()
        self.activity_feed = []

    def add_credit_card(self, card_number, limit):
        self.credit_card = self.credit_card or CreditCard(card_number, limit)

    def pay(self, recipient, amount, description=""):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.activity_feed.append(f"{self.username} paid {recipient.username} ${amount:.2f} for {description}")
            recipient.activity_feed.append(f"{self.username} paid {recipient.username} ${amount:.2f} for {description}")
        elif self.credit_card and self.credit_card.charge(amount):
            recipient.balance += amount
            self.activity_feed.append(f"{self.username} used credit card to pay {recipient.username} ${amount:.2f} for {description}")
            recipient.activity_feed.append(f"{self.username} used credit card to pay {recipient.username} ${amount:.2f} for {description}")
        else:
            print("Insufficient funds or credit limit reached")

    def retrieve_activity(self):
        return self.activity_feed

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.add(friend)
            friend.friends.add(self)
            self.activity_feed.append(f"{self.username} added {friend.username} as a friend")
            friend.activity_feed.append(f"{self.username} added {friend.username} as a friend")
