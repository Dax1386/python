import random

choices = ["rock", "paper", "scissors"]
running = True

while running:
    player = None
    computer = random.choice(choices)

    
    while player not in choices:
        player = input("Enter your choice (rock, paper, scissors): ").lower()
        if player not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win! Rock beats scissors.")
    elif player == "paper" and computer == "rock":
        print("You win! Paper beats rock.")
    elif player == "scissors" and computer == "paper":
        print("You win! Scissors beats paper.")
    else:
        print("You lose!")

    if not input("Do you want to play again? (yes/no): ").lower() == "yes":
        running = False

print("Thanks for playing!")