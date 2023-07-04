# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# print
# calc
# convert
# if else elif

number1 = float(height)
number2 = float(weight)

calc = (number2 / number1 ** 2)
round = int(calc)
print("Your BMI is:",(round))

if round < 18.5:
  print(f"Your BMI is {round}, you are underweight.")