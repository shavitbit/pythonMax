# This is a sample Python script with basic information.
# to run part of the script use control shift e
print("hello max")
print("*" * 10)
print(); print()
# string
var_str_name = "oren"
print("My name is "+ var_str_name + ".")
# bool
var_bool_true = True

# float
var_float = 10.4
# input and \n for new line
last_name=input("Enter your last name\n")
print("Your last name is " + last_name)


# convert string to int and then int to string
birth_year=input("Birth year?\n")
# check what type of var is it
print(type(birth_year))
age = 2020-int(birth_year)
print(type(age))
print("You are "+ str(age) + " Years old.")

# Multiple line of string
multi_line = """
Hi Oren, 
this is my msg
your last name is """ + last_name + """
and you are """+str(age)+""" years old 
the end.

"""
print(multi_line)
# Substring from 0 to 9 in the string multi_line
print(multi_line[0:9])
# from 5 to end
from5_2_end = multi_line[5:]
# from 0 to 5
from0_2_5 = multi_line[:5]
# Only the the second char from the end
second_from_end = multi_line[-2]

# split method
str1 = "Good morning israel"
str2 = str1.split(" ")
print(str2[1])


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



