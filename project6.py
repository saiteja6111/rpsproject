#lets do a rock, paper and scissor game
import random

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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

value_list = [rock,paper,scissor]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. : "))
computer_choice = random.choice([0,1,2])

print(value_list[user_choice])
print("computer choice: ")
print(value_list[computer_choice])

if user_choice == computer_choice:
    print('Draw')
elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
    print('You Lost')
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print('You WON')
else:
    print('Enter correct choice!')




