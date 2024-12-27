# Write a program that uses a multiply function to multiply two numbers and returns the result. 
# Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

# $ python multiply.py
# Enter the first number: 3.1416
# Enter the second number: 2.7183
# 3.1416 * 2.7183 = 8.53981128

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
result = float(first_number) * float(second_number)

print(f"{first_number} * {second_number} = {result}")