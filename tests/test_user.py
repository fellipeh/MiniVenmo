from user import User
from credit_card import CreditCard

def test_user_creation():
    user = User("Alice", 100)
    assert user.username == "Alice"
    assert user.balance == 100
    assert user.credit_card is None
    assert user.friends == set()
    assert user.activity_feed == []

def test_add_credit_card():
    user = User("Alice")
    user.add_credit_card("1234-5678-8765-4321", 200)
    assert isinstance(user.credit_card, CreditCard)
    assert user.credit_card.number == "1234-5678-8765-4321"
    assert user.credit_card.limit == 200

def test_pay_with_balance():
    user1 = User("Alice", 100)
    user2 = User("Bob", 50)
    user1.pay(user2, 30, "Dinner")
    assert user1.balance == 70
    assert user2.balance == 80
    assert "Alice paid Bob $30.00 for Dinner" in user1.activity_feed
    assert "Alice paid Bob $30.00 for Dinner" in user2.activity_feed


def test_pay_with_credit_card():
    user1 = User("Alice", 100)
    user2 = User("Bob", 50)
    user1.add_credit_card("1234-5678-8765-4321", 200)

    user1.pay(user2, 150, "Concert")

    assert user1.credit_card.balance == 50
    assert user2.balance == 200
    assert "Alice used credit card to pay Bob $150.00 for Concert" in user1.activity_feed
    assert "Alice used credit card to pay Bob $150.00 for Concert" in user2.activity_feed

def test_add_friend():
    user1 = User("Alice")
    user2 = User("Bob")
    user1.add_friend(user2)
    assert user2 in user1.friends
    assert user1 in user2.friends
    assert "Alice added Bob as a friend" in user1.activity_feed
    assert "Alice added Bob as a friend" in user2.activity_feed
