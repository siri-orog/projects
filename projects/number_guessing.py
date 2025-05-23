import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    lower_bound = 1  # Set lower limit
    upper_bound = 100  # Set upper limit
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 5  # Limit number of attempts

    print(f"\nI have selected a number between {lower_bound} and {upper_bound}.")
    print(f"You have {attempts} attempts to guess it correctly.\n")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
            if guess < lower_bound or guess > upper_bound:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
                continue
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} correctly!")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    else:
        print(f"❌ Game over! The correct number was {secret_number}.")

    # Option to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        number_guessing_game()
    else:
        print("Thanks for playing! See you next time. 😊")

# Start the game
number_guessing_game()