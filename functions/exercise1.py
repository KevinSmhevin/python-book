#What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# get an error because foo is undefined in the globl scope