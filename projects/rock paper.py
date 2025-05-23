import random

# Possible choices
choices = ["rock", "paper", "scissors"]

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Main Game Loop
while True:
    player_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    
    if player_choice == "exit":
        print("Thanks for playing! Goodbye!")
        break
    elif player_choice not in choices:
        print("Invalid choice, please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    result = get_winner(player_choice, computer_choice)
    print(result)