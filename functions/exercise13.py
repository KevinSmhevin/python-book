def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)


# will throw a type error for missing required argument

# nondefault argument follows default argument