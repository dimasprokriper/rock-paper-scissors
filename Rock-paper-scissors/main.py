import random

rps_choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(rps_choices)
player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
if player_choice not in rps_choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
elif player_choice == computer_choice:
    print(f"Both players selected {player_choice}. It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"): 
    print(f"You chose {player_choice} and the computer chose {computer_choice}. You win!")