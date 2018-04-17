'''Post SLO Test v1.0 By Andrew Ault
4/17/18
'''
print("Hello and welcome to Budget Calculator! (Press Enter to move on)")
input()
fname = input("What is your first name? ")
lname = input("What is your last name? ")
print("Hello, " + fname + " " + lname)
while True:
    budget = input("Please enter your daily budget: ")
    try:
        budget = float(budget)
        break
    except:
        print("Oof thats not a valid number!")
        continue
while True:
    breakfast = input("How much did you spend on Breakfast?: ")
    try:
        breakfast = float(breakfast)
        break
    except:
        print("Oof thats not a valid number!")
        continue
while True:
    lunch = input("How much did you spend on lunch? ")
    try:
        lunch = float(lunch)
        break
    except:
        print("Oof not a valid number!")
        continue
while True:
    dinner = input("How much did you spend on Dinner? ")
    try:
        dinner = float(dinner)
        break
    except:
        print("Oof not a valid number!")
        continue
total = breakfast + lunch + dinner
print("You spent a total of $" + str(total))
totalaverage = total / 3
print("Your average meal cost is $" + str(totalaverage))
remaining = budget - total
print("You have $" + str(remaining) + " remaining")