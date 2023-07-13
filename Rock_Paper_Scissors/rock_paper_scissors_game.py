import random 


def structure_choices():
    player_one_choice = input("Enter a Choice Rock, Paper, Scissors: ")
    options = ["Rock", "Paper", "Scissors"]
    computer_bot_choice = random.choice(options)
    choices = {"player": player_one_choice, "computer": computer_bot_choice}
    return(choices)


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a Tie (-_-)"
    elif player == "Rock":
        if computer == "Scissors":
            return "Rock beats Scissors. You win!"
        else:
            return "Paper covers Rock. You lose."
    elif player == "Paper":
        if computer == "Rock":
            return "Paper covers Rock. You win!"
        else:
            return "Scissors cuts Paper. You lose."
    elif player == "Scissors":
        if computer == "Paper":
            return "Scissors cuts Paper. You win!"
        else:
            return "Rock smashes Scissors. You lose."
    else:
        return "Invalid input. Please choose Rock, Paper, or Scissors."


choices = structure_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
