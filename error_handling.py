
# the input accept only int and by giving him char or string
# the code will jump to except value error
try:
    age = int(input('age: '))
    print(age)
    income = 300
    risk = income / age
except ValueError:
    print('invalid value')
except ZeroDivisionError:
    print('You cannot divide by zero')

# try to enter string as age instead of integer
# try to enter 0 as age for  ZeroDivisionError
