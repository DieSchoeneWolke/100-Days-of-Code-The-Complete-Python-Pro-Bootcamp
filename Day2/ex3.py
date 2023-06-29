# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#convert datatype
#convert years
#calc
#print f string
#set reachable age and calc from there

# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# Reachable age 85

convert1 = int(age)
reachable_age =  85 - (convert1)

days = (reachable_age)  * 365
weeks = (reachable_age)  * 52
months = (reachable_age)  * 12
print(f"You have {days} days, {weeks} weeks, {months} months left until becoming 85.")

