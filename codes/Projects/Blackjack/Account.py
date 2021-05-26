class Account:
    """
    Class for the account of the player.
    """

    def __init__(self, balance, name="Player"):
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print(f"New balance is {self.balance}.")

    def debit(self, amount):
        if amount > self.balance:
            print("Not enough chips!")
            print(f"Your current chip balance is {self.balance}.")
            return True
        else:
            self.balance -= amount
            print(f"Your remaining balance is: {self.balance}.")
            return False

    def __str__(self):
        return f"{self.name.title()} has total chip {self.balance}."
