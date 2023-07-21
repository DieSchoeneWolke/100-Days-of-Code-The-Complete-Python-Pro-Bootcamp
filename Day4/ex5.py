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
user_input = int(input("1 for 🧱, 2 for 📃, 3 for ✂"))
user_input -= 1  # Decrement user_input by 1 to fit the 0-based index

#Print image for user
print (img[user_input])

#Add random integer as AI
ai_decision = random.randint(0, 2)
