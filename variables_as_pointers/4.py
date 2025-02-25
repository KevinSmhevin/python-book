# Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

'''
it will print [1, 42, 3] because dict2 creates a shallow copy of dict1
so the list of 'a' in both dictionaries reference the same list in memory
'''