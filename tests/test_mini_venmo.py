from main import MiniVenmo


def test_create_user():
    app = MiniVenmo()
    app.create_user("Alice", 100)
    assert "Alice" in app.users
    assert app.users["Alice"].username == "Alice"
    assert app.users["Alice"].balance == 100


def test_render_feed():
    app = MiniVenmo()
    app.create_user("Alice", 100)
    app.create_user("Bob", 50)

    alice = app.users["Alice"]
    bob = app.users["Bob"]

    alice.add_credit_card("1234-5678-8765-4321", 200)
    alice.add_friend(bob)

    alice.pay(bob, 30, "Dinner")
    bob.pay(alice, 15, "Movie")

    feed = app.render_feed()
    assert "Alice added Bob as a friend" in feed
    assert "Alice paid Bob $30.00 for Dinner" in feed
    assert "Bob paid Alice $15.00 for Movie" in feed
