# Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

'''
it will print {42, 'Monty Python', ('a', 'b', 'c'), range(5,10)}
because set2 is pointing to the same set in memory as set1
'''