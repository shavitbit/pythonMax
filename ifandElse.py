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
