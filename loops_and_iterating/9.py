'''
Write a function that computes and returns the factorial of a number by using a for or while loop. 
The factorial of a positive integer n, signified by n!, 
is defined as the product of all integers between 1 and n, inclusive:

'''

def factorial(n):
    total = 1
    i = 1
    while i < n:
        i += 1
        total *= i
    return total

print(factorial(5))



def for_factorial(n):
    total = 1
    for num in range(1, n + 1):
        total *= num
    
    return total

print(for_factorial(5))