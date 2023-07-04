# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# print
# calc
# convert
# if else elif

calc = round(weight / height ** 2)

if calc < 18.5:
  print(f"Your BMI is {calc}, you are underweight.")