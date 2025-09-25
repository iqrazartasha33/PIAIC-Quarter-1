# Class 2
# Topic: Python Variables and Data Types
print("Welcome to Class 2")

# -------------------------
# Variables
name = "Iqra"
number = 25
print(number)   # Output: 25
print(name)     # Output: Iqra

# -------------------------

# Data Types 

# 1) String -> str
print("Iqra")   # Output: Iqra

# 2) Integer -> int
print(25)       # Output: 25

# 3) Float -> float
print(5.5)      # Output: 5.5

# 4) Boolean -> bool -> True / False
print(False)    # Output: False
print(True)     # Output: True

# 4) List
x = "hello"
print(list(x))   # ['h', 'e', 'l', 'l', 'o']

# 5) Tuple
x = "hello"
print(tuple(x))  # ('h', 'e', 'l', 'l', 'o')

# 6) Set
x = "hello"
print(set(x))    # {'h', 'e', 'o', 'l'}

# 7) Dictionary
data = [("name", "Iqra"), ("age", 18)]
print(dict(data))  # {'name': 'Iqra', 'age': 18}

# 8) Range
print(list(range(1, 13)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# -------------------------

# Operators in Python
# 1) Arithmetic Operators
# 2) Comparison Operators
# 3) Assignment Operators
# 4) Logical Operators

# -------------------------

# 1) Arithmetic Operators
print(5 + 2)     # Addition -> 7
print(10 - 6)    # Subtraction -> 4
print(20 * 8)    # Multiplication -> 160
print(40 / 4)    # Division -> 10.0
print(10 % 3)    # Modulus -> 1
print(10 // 3)   # Floor Division -> 3
print(2 ** 3)    # Exponentiation -> 8

# -------------------------

# 2) Comparison Operators
num1 = 10
num2 = 5

print(num1 == num2)   # False
print(num1 > num2)    # True
print(num1 < num2)    # False
print(num1 != num2)   # True
print(num1 >= num2)   # True
print(num1 <= num2)   # False

# -------------------------

# 3) Assignment Operators
num1 = 10

# Long way (normal assignment)
num2 = num1 + 5  
print(num2)   # 15

num3 = num1 - 5
print(num3)   # 5

num4 = num1 * 5
print(num4)   # 50

num5 = num1 / 5
print(num5)   # 2.0

# Short way (compound assignment operators)

x = 10
x += 5   # x = x + 5
print(x)  # 15

x -= 3   # x = x - 3
print(x)  # 12

x *= 2   # x = x * 2
print(x)  # 24

x /= 4   # x = x / 4
print(x)  # 6.0

# -------------------------

# 4) Logical Operators

a = True
b = False

print(a and b)   # False (Both True hona zaroori hai)
print(a or b)    # True  (Ek bhi True hoga to True)
print(not a)     # Output: False (Because NOT True = False)
print(not b)     # Output: True  (Because NOT False = True)
