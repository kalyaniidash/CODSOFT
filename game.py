import random
def get_computer_choice():
    choices =["rock","paper","scissors"]
    return random.choice(choices)
def get_user_choice():
    choice =input("Enter your choice (rock/paper/scissors):").lower()
    while choice not in ["rock","paper","scissor"]:
        print("Invalid choice.Please try again")
        choice =input("Enter your choice(rock/paper/scissors)").lower()
    return choice
def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return"It's a tie!"
    elif (user_choice =="rock" and computer_choice == "scissors") or \
         (user_choice =="scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"
def main():
    print("Welcome to Rock,Paper,Scissors!")
    while True:
        user_choice =get_user_choice()
        computer_choice =get_computer_choice()
        print(f"you choose :{user_choice}")
        print(f"computer choose: {computer_choice}")

        result =determine_winner(user_choice,computer_choice)
        print(result)

        play_again =input("Do you want to play again(yes/no):").lower()
        if play_again !="yes":
            print("Thank you for plaing! Good Bye!")
            break
if __name__ == "__main__":
    main()