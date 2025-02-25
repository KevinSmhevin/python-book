# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# first line is slicing the original string from index 21-35 and returning the index of f in the sliced string
# second string is returning the index of f from the original string but only looking from index 21 - 35