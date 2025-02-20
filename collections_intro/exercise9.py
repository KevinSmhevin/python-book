my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

'''
Given the above code, answer the following questions and explain your answers:

Are the lists assigned to my_list and another_list equal? 
    yes they are equal because because they have the same values
Are the lists assigned to my_list and another_list the same object?
    no they are not the same object, another_list is a new instance of an object
Are the nested lists at index 3 of my_list and another_list equal?
    yes they have the same values
Are the nested lists at index 3 of my_list and another_list the same object?
    they are the same object since the constructor creates a shallow copy 
'''

