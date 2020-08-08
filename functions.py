def max_func():
    print('hi max')
    print("im am printing you from a function")


print("start")
max_func()
print("finish")


# pass information for function (void)
def max_func_pass(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')

    print("im am printing you from a function")


max_func_pass('Oren', 'bahar')
max_func_pass(last_name="Bahar", first_name="Oren")


# function that return value
def square(number):
    """

    :type number: int
    """
    return number * number


result = square(3)
print(result)

print(square(3))
