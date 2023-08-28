rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random  #importing random lib

#taking user choice as input
user_choice = input("What do you choose?Type 0 for rock, 1 for paper, 2 for scissors\n")

#printing different patterns according to user's choice
if user_choice == '0':
  print("You choosed'ROCK' \n",rock)
elif user_choice == '1':
  print("You choosed 'PAPER' \n",paper)
elif user_choice == '2':
  print("You choosed 'SCISSORS' \n",scissors)
else:
  print("Invalid choice!")

#creating gamelist to take computers random choice by using len() function
game_list = [rock, paper, scissors]
comp_choice = str(random.randint(0, len(game_list) - 1))

#printing different patterns according to computers choice
if comp_choice == '0':
  print("Computer: 'ROCK'", rock)
elif comp_choice == '1':
  print("Computer: 'PAPER'",paper)
elif comp_choice == '2':
  print("Computer: 'SCISSORS'",scissors)

#if user choose 'ROCK' than checking the rsult with different options computer could choose!
if user_choice == '0' and comp_choice == '0':
  print("DRAW")
elif user_choice == '0' and comp_choice == '1':
  print("YOU LOST!")
elif user_choice == '0' and comp_choice == '2':
  print("YOU WON!")

#if user choose 'PAPER' than checking the result with different options computer could choose!
elif user_choice == '1' and comp_choice == '0':
  print("YOU WON!")
elif user_choice == '1' and comp_choice == '1':
  print("DRAW")
elif user_choice == '1' and comp_choice == '2':
  print("YOU LOST!")

#if user choose 'SCISSORS' than checking the result with different options computer could choose!
elif user_choice == '2' and comp_choice == '0':
  print("YOU LOST!")
elif user_choice == '2' and comp_choice == '1':
  print("YOU WON!")
elif user_choice == '2' and comp_choice == '2':
  print("DRAW")