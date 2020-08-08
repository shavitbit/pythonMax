is_hot = True
is_cold = not is_hot

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("Its a cold day")
    print("Wear warm cloth")
print("Enjoy your day")

print(is_cold)

# else if use

if is_hot == is_cold:
    print("You cannot enter here because its false")
elif is_hot != is_cold:
    print("That's a true expression.")


# if a person has high income AND good credit
#   the person is eligible for loan
# if a person has apple or orange one of them or both
# print person is fat
has_high_income = True
has_good_credit = True

if has_good_credit and has_high_income:
    print("Eligible for loan")

apple = True
orange = False
if apple or orange:
    print("i have apple or orange or both")


# ><= !
temperature = 30
# bigger or equal
if temperature >= 30:
    print("its a hot day")
else:
    print("its not a hot day")

