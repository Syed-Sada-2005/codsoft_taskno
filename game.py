import random

# Function to determine the winner for one round of Rock-Paper-Scissors
def determine_winner(user_choice, computer_choice):
    # Define the rules: rock beats scissors, scissors beat paper, paper beats rock
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Main function to play the game
def play_game():
    user_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']
    
    print("Welcome to Rock-Paper-Scissors game!")
    print("Enter your choice: rock, paper, or scissors. To quit, enter 'quit'.")
    
    while True:
        # User input
        user_choice = input("Your choice: ").lower()
        
        if user_choice == 'quit':
            break
        
        # Check if user input is valid
        if user_choice not in choices:
            print("Invalid input. Please enter rock, paper, or scissors.")
            continue
        
        # Computer randomly selects
        computer_choice = random.choice(choices)
        
        # Determine the winner for this round
        result = determine_winner(user_choice, computer_choice)
        
        # Display choices and result
        print("You chose: {user_choice}")
        print("Computer chose: {computer_choice}")
        print(result)
        
        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        # Display current score
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        print("------------------------")
    
    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()