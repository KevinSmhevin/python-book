# What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')


# nothing since the function returns before it prints anything, and it doesnt return anything