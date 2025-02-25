# What will the following code print?

print('abc-def'.isalpha()) #false
print('abc_def'.isalpha()) #false
print('abc def'.isalpha()) #false
print('abc def'.isalpha() and
      'abc def'.isspace()) #false
print('abc def'.isalpha() or
      'abc def'.isspace()) #false
print('abcdef'.isalpha()) #true
print('31415'.isdigit()) #true
print('-31415'.isdigit()) #false
print('31_415'.isdigit()) #false
print('3.1415'.isdigit()) #false
print(''.isspace()) #false