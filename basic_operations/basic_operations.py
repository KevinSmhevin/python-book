# 1. Concatenate two strings, one with your first name and one with your last, 
# to create a new string with your full name as its value. 
# #For example, if your name is John Doe, 
# #you should combine 'John' and 'Doe' to get 'John Doe'.

first = 'Kevin'
last = 'Paras'
name = first + ' ' + last

print(name)

# 2. Use the REPL and the arithmetic operators to extract the individual digits of 4936:
# One place is 6.
# Tens place is 3.
# Hundreds place is 9.
# Thousands place is 4.

num = 4936
multiplier = 10
for i in range(4):
    digit = num % multiplier
    print(f"current digit is {digit}")
    num //= multiplier
    
    
# 3. What does the following code do? Why?
# print('5' + '10')

# prints '15' because string concatenation instead of adding 2 integers 

# 4. Refactor the code from the previous exercise to use coercion to print 15 instead.

print(int('5') + int('10')) 

# 5. Will an error occur if you try to access a list 
# element with an index greater than or equal to the list's length? For example:
# foo = ['a', 'b', 'c']
# print(foo[3])      # will this result in an error?

# yes because list index start at 0 so foo[3] does not exist 

# 6 To what value does the following expression evaluate?
# 'foo' == 'Foo'

# false , case sensitivity matters 

# 7 What will the following code do? Why?
# int('3.1415')

# throws a value error since the provided input is not a valid integer

# To what value does the following expression evaluate?
# '12' < '9'

# true since 1 is less than 9 py -3.12 -m jupyter notebook






