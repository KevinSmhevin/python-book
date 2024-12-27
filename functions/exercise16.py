# In the code shown below, identify all of the function names and parameters present in the code. 
# Include the line numbers for each item identified.


def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')


#functions 
#   multiply - line 5, 13
#   get_num - line 8,11,12
#   float - line 9 
#   print - line 14

#parameters left, right - line 5, prompt - lne 8