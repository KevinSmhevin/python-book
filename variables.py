# 1 Classify the following potential non-constant variable names as idiomatic, non-idiomatic, or illegal. 
# For the non-idiomatic and illegal names, explain your choice.

# Name --> non idiomatic --> N should be lowercase
# index --> idiomatic
# CatName --> non idiomatic --> should be snake_case
# lazy_dog --> idiomatic
# quick_Fox --> non idiomatic --> F should be lower case
# 1stCharacter --> illegal --> 1st character cant be digit
# operand2 --> nonidiomatic --> should be snake_case
# BIG_NUMBER --> idiomatic --> wrong (i thought constants should use screaming snake case)
# π -->  non idiomatic --> not an ASCII character

# 2 Classify the following potential function names as idiomatic, non-idiomatic, or illegal. 
# For the non-idiomatic and illegal names, explain your choice.

# Name          --> non idiomatic - N should be lowercase
# index         --> idiomatic
# CatName       --> non diomatic - should be snake case
# lazy_dog      --> idiomatic
# quick_Fox     --> non idiomatic - same as above
# 1stCharacter  --> illegal
# operand2      --> idiomatic
# BIG_NUMBER    --> non idiomatic
# π             --> non idiomatic

# 3 Classify the following potential constant names as idiomatic, non-idiomatic, or illegal. 
# For the non-idiomatic and illegal names, explain your choice.

# index     --> non idiomatic - should not use lowercase
# CatName   --> non idiomatic - should not use lowercase
# snake_case    --> non idiomatic - should not use lowercase
# LAZY_DOG3     --> idiomatic
# 1ST           --> illegal - first character should not use digit 
# operand2      --> non idiomatic - should not use lowercase
# BIG_NUMBER    --> idiomatic
# Π             --> non idiomatic - not ASCII

# 4 Classify the following potential class names as idiomatic, non-idiomatic, or illegal. 
# For the non-idiomatic and illegal names, explain your choice.

# index         --> non idiomatic - i should be uppder
# CatName       --> idiomatic
# Lazy_Dog      --> non idiomatic - should not be snake case
# 1ST           --> illegal - no 1st digit
# operand2      --> non idiomatic - should be pascal case
# BigNumber3    --> idiomatic
# Π             --> non idiomatic - none ASCII


# Challenge: This program uses a bit of math. Don't let that scare you away -- try it anyway.

# Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank 
# that pays you 5% (this is a wish-fulfillment fantasy) compounded interest every year. 
# After one year, you will have $1,050 ($1,000 times 1.05). After two years, 
# you will have $1,050 times 1.05, or $1102.50. 
# Create a variable named balance that contains 
# the amount of money you will have after 5 years, then print the result. 
# Use a single expression if you can to set balance to the correct value.


balance = 1000 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05

print(balance)

balance = 1000
for i in range(5):
    balance *= 1.05
    
print(balance)