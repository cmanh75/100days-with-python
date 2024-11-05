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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

my_move = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors "))

move = [rock, paper, scissors]

print(move[my_move])

computer_move = random.randint(0, 2)

print(f"Computer choose: \n {move[computer_move]}")

if (my_move == computer_move):
    print("Draw")
elif ((my_move + 1) % 3 == computer_move):
    print("You lose")
else:
    print("You win")

