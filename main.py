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

# Write your code below this line 👇
import random

choices = ["rock", "paper", "scissors"]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer = random.randint(0, 2)

print(choices[user])
if user == 0:
    print(rock)
elif user == 1:
    print(paper)
else:
    print(scissors)

print(choices[computer])
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

if user == 0 and computer == 2:
    print("You Win!")
elif user == 2 and computer == 1:
    print("You Win!")
elif user == 1 and computer == 0:
    print("You Win!")
elif user == computer:
    print("Its Draw!")
else:
    print("Computer Win")



