import random

# Intoduction
print("Welcome to the Rock, Paper and Scissors Game!!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

# Validate user input
if  0 <= user_choice <= 2:
    # Generate computer choice
    computer_choice = random.randint(0, 2)

    # Map choices to their names
    choices = ["Rock", "Paper", "Scissors"]
    user_choice_name = choices[user_choice]
    computer_choice_name = choices[computer_choice]
    
    # Display choices
    print(f"\nYou chose: {user_choice_name}")
    print(f"Computer chose: {computer_choice_name}")
    
    # Outcome logic
    if user_choice == computer_choice:
        print("\nIt's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
        (user_choice == 1 and computer_choice == 0) or \
        (user_choice == 2 and computer_choice == 1):
        print("\nYou won!!")
    else:
        print("\nYou lose...")
else:
    print("Type a valid number")