# What does this program print? Why?

foo = 'bar'

def set_foo():
    foo = 'qux'
    
set_foo()
print(foo)


# line 9 prints bar since bar is what is defined in the global scope for that variable