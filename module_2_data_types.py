"""
Description: A script to demonstrate data types.
Author: Damien Altenburg
Date: 9/9/2024
Usage: python module_2_data_types.py
"""
# print syntax
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print("Hello world", "Damien", sep =',')

print(type(25))

student_full_name = "Damien Altenburg"

# age (int)
user_age = 26

print(type(user_age))

# java
# int personAge;

# current salary (float)
employee_current_salary = 34567.99

print(type(employee_current_salary))

# are you employed (bool)
is_employed = True

print(type(is_employed))

# Attempt to use a word that was not declared
#print(favorite_color)

PI = 3.14159
NUMBER_OF_MONTHS_IN_A_YEAR = 12

# 5%
FEDERAL_TAX_RATE = 0.05

# Java
# final float FEDERAL_TAX_RATE = 0.05;

print(PI, FEDERAL_TAX_RATE)

# Syntax
# input(prompt_text)

users_name = input("What is your name? ")

#print(users_name)

user_age = input("What is your age? ")

#print(user_age)

#print(type(user_age))

# f-string
print(f"Hello {users_name}, you are {user_age} years old.")

# Escape Sequence
# "\symbol"
print(f"\tValue of\n\nPI: {PI:.2f}")

# "Damien"
print("\"Damien\"")

print(PI)
