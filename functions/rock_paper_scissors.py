# Assuming Rock is 0, Paper is 1 and Scissors 2
def rock_paper_scissors(playerOne, PlayerTwo):
    """Returns the winner of the Rock, Paper or Scissors game. Rock is 0, Paper is 1 and Scissors is 2."""
    """Rock beats Scissors, Scissors beats Paper and Paper beats Rock."""
    if playerOne == PlayerTwo:
        return "It's a Draw!"
    elif playerOne == 0 and PlayerTwo == 1:
        return "Player 2 Wins"
    elif playerOne == 0 and PlayerTwo == 2:
        return "Player 1 Wins"
    elif playerOne == 1 and PlayerTwo == 0:
        return "Player 1 Wins"
    elif playerOne == 1 and PlayerTwo == 2:
        return "Player 2 Wins"
    elif playerOne == 2 and PlayerTwo == 0:
        return "Player 2 Wins"
    elif playerOne == 2 and PlayerTwo == 1:
        return "Player 1 Wins"
