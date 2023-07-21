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

import random

#List of images
img = [rock, paper, scissors]

#Prompt user
user_input = int(input("1 for 🧱, 2 for 📃, 3 for ✂\n"))
user_input -= 1  # Decrement user_input by 1 to fit the 0-based index

#Print image for user
print (img[user_input])

#Add random integer as AI
ai_decision = random.randint(0, 2)
ai_decision -= 1

#Print image for AI
print ("VS.")
print(img[ai_decision])

#Gamelogic
if user_input == 0 and ai_decision == 2:
    print("Winner!")
elif ai_decision == 0 and user_input == 2:
    print("Loser!")
elif ai_decision > user_input:
    print("Loser!")
elif user_input > ai_decision:
    print("Winner!")
elif ai_decision == user_input:
    print("Draw!")
