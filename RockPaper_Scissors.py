
import random
#Define ASCII art for Rock,Paper, and scissors hands
rock_hand = r"""
      _______
 ----'   ____)
        (_____)
        (_____)
        (____)
 ---.__(____)      
  """
paper_hand = r"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors_hand = r"""
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""
game_images=[rock_hand,paper_hand,scissors_hand]

while True:
    user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissor:"))
    if user_choice >= 3 or user_choice < 0:
        print("Invalid Number,You Lose.")
    else:
        print(game_images[user_choice])
        computer_choice=random.randint(0,2)
        print("Computer_choice")
        print(game_images[computer_choice])
        if computer_choice == user_choice:
            print("It's a Tie")
        elif computer_choice == 0 and user_choice == 2:
            print("You Lose.")
        elif user_choice == 0 and computer_choice == 2:
            print("you Win.")
        elif computer_choice > user_choice:
            print("You Lose.")
        elif user_choice > computer_choice:
            print("You win.")


    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for Playing!")
        break


