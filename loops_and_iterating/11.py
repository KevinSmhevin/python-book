'''
Print all of the even numbers in the following list of nested lists. 
This time, don't use any for loops.

'''


my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

outer_index = 0
evens = []
while outer_index < len(my_list):
    inner_index = 0
    while inner_index < len(my_list[outer_index]):
        num = my_list[outer_index][inner_index]
        if num % 2 == 0:
            evens.append(num)
            
        inner_index += 1
        
    outer_index += 1
    
print(evens)


result = [num for inner_list in my_list for num in inner_list if num % 2 == 0]

print(result)