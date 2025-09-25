# Class 3
# Topic: Python (if, else, elif statements) and
# Class Task: Grading System with if-elif-else

# Variables
fav_game = "Cricket"
fav_food = "Biryani"
age = True
print(fav_game, id(fav_game))

# if-else example
isRaining = True

if isRaining:
    print("No school today")
else:
    print("Go to school")

# Voting check
age = 15

print(age == 18)  # False
print(age < 18)   # True

if age == 18:
    print("You can vote")
else:
    print("You cannot vote")

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

# elif example
number = 10

if number > 10:
    print("Number is greater than 10")
elif number == 10:
    print("Number is equal to 10")
else:
    print("Number is less than 10")

# Class Task:
#  Grading System

percentage = int(input("Enter your percentage: "))

if percentage >= 80 and percentage <= 100:
    print("A+1 Grade")
elif percentage >= 70 and percentage < 80:
    print("A Grade")
elif percentage >= 60 and percentage < 70:
    print("B Grade")
elif percentage >= 50 and percentage < 60:
    print("C Grade")
elif percentage >= 40 and percentage < 50:
    print("D Grade")
else:
    print("Fail")
