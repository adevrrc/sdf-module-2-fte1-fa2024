"""
Description: A script to calculate the average of three integers
             entered by the user in the terminal.
Author: Damien Altenburg
Date: 2024-9-16
Usage: python calculate_average.py
"""
NUMBER_OF_INPUTS = 3

first_number_input = input("Enter first number: ")
first_number_input = int(first_number_input)

second_number_input = input("Enter second number: ")
second_number_input = int(second_number_input)

third_number_input = input("Enter third number: ")
third_number_input = int(third_number_input)

sum = first_number_input + second_number_input + third_number_input

# Calculate the average
average = sum / NUMBER_OF_INPUTS

print(f"The average is {average:.1f}.")
