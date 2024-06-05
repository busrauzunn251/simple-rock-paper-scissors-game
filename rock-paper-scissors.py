import random

def select_winner(player,computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer== 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "Player wins!"
    else:
        return "Computer wins!"
    
while True:
    print("\nWelcome to the Rock-Paper-Scissors game!")
    player_choice = input("Rock, paper or scissors? (Press 'q' to quit):").lower()


    if player_choice == 'q':
        print("Exit")
        break
    
    if player_choice not in ['rock','paper','scissors']:
        print("Please choose 'rock','paper', or 'scissors'!")
        continue

    computer_choice = random.choice(['rock','paper','scissors'])

    print(f"\nPlayer's choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(select_winner(player_choice,computer_choice))