class Actions:
    """
    Class for the possible action a player can take during the game
    """

    def __init__(self):
        pass

    def ask_bet(self):
        """
        Ask the player for bet money
        """
        while True:
            bet = input("How many chips do you want to bet? ")
            if not bet.isdigit():
                print("Please provide valid responce")
            else:
                bet = int(bet)
                break
        return int(bet)

    def ask_balance(self):
        """
        Ask for the player's chip balance
        """
        while True:
            balance = input("What is your current chip? ")
            if not balance.isdigit():
                print("Please provide valid responce")
            else:
                balnce = int(balance)
                break
        return int(balance)

    def start_play(self):
        """
        Ask To start playing the game
        """
        while True:
            value = input(
                "Do you want to play the game? Type 'y' for Yes and 'n' for No "
            )
            if value.lower() not in ["y", "n"]:
                print("Please provide valid responce")
            else:
                break
        return value.lower() == "y"

    def ask_replay(self):
        """
        Ask the player if he wants to replay the game
        """
        while True:
            value = input("Do you want to replay? Type 'y' for Yes and 'n' for No ")
            if value.lower() not in ["y", "n"]:
                print("Please provide valid responce")
            else:
                break
        return value.lower() == "y"

    def stand_or_hit(self):
        """
        Ask the player to hit or stand
        """
        while True:
            decision = input("Do you want to 'stand' or 'hit'? Type 's' or 'h': ")
            if decision.lower() not in ["s", "h"]:
                print("Please type 's' or 'h' for stand or hit.")
            else:
                break
        return decision.lower()

    def adjust_ace(self):

        """
        Ask the player to use the value of Ace
        """
        while True:
            decision = input("Do you want to the value of Ace as 1 or 11? ")
            if decision.lower() not in ["1", "11"]:
                print("Please type '1' or '11'.")
            else:
                break
        return decision == "1"
