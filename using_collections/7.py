# Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

# new_info = []
# for char in info:
#     if char == ':':
#         new_info.append('+')
    
#     else:
#         new_info.append(char)

new_info = info.split(':')
    
info = '+'.join(new_info)

print(info)

# Try this problem using the methods you've learned about in this chapter. 
# Once you have that working, use the Python documentation for the str type to find an alternative solution.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'


new_info = info.replace(':', '+')

print(new_info)