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
import random
answer = input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if answer == "0" :
    print(rock)
elif answer == "1":
    print(paper)
elif answer == "2":
    print(scissors)

list_choice  = [rock,paper,scissors]
random_choice = random.choice(list_choice)
print("computer choose :")
print(random_choice)

if answer == "0":
    if random_choice == rock:
        print("Draw")
    elif random_choice == paper:
        print("you lose")
    elif random_choice == scissors:
        print("you win")
elif answer == "1":
    if random_choice == rock:
        print("you win")
    elif random_choice == paper:
        print("Draw")
    elif random_choice == scissors:
        print("you lose")
elif answer == "2":
    if random_choice == rock:
        print("you lose")
    elif random_choice == paper:
        print("you win")
    elif random_choice == scissors:
        print("Draw")
else:
    print("you type shit get lost")
