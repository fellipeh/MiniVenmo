from user import User


class MiniVenmo:
    def __init__(self):
        self.users = {}

    def create_user(self, username, balance=0):
        self.users.setdefault(username, User(username, balance))

    def render_feed(self):
        return "\n".join(activity for user in self.users.values() for activity in user.retrieve_activity())


if __name__ == "__main__":
    app = MiniVenmo()

    # Create users
    app.create_user("Alice", 100)
    app.create_user("Bob", 50)

    # Add credit cards
    alice = app.users["Alice"]
    bob = app.users["Bob"]
    alice.add_credit_card("1234-5678-8765-4321", 200)

    # Add friends
    alice.add_friend(bob)

    # Users make payments
    alice.pay(bob, 30, "Dinner")
    bob.pay(alice, 15, "Movie")

    # Print activity feed
    print(app.render_feed())
