# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#len function
#random integer
#list data structure

int_rng = len(names)

rng = random.randint(0, int_rng - 1)
