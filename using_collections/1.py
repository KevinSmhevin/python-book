# Write Python code to print the seventh number of range(0, 25, 3).

counter = 1
for i in range(0, 25, 3):
    if counter == 7:
        print(i)
        break
    counter += 1
    
    
seventh = range(0, 25, 3)[6]
print(seventh)