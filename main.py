import random

def play():
    options = ["rock", "paper", "scissors"]
    
    while True:
        player = input("Choose rock, paper, or scissors: ").lower()
        if player not in options:
            print("Invalid choice, please try again.")
            continue
        
        computer = random.choice(options)
        print(f"The computer chose: {computer}")
        
        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "scissors" and computer == "paper") or \
             (player == "paper" and computer == "rock"):
            print("You win!")
        else:
            print("You lose.")
        
        # Ask if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Call the function to start the game
play()