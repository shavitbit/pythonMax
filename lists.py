names = ["Oren", "Tal", "Shlomi"]
print(names[0])
print(names[-1])
# from item [1] to the end
print(names[1:])
# for the length of the list
print(len(names))
# add to the end of the list
names.append("Erez")
print(names)
# add to the middle of the list
names.insert(2,"Meggie")
print(names)
# find the index of oren in the list
print("the index of Oren is: "+str(names.index("Oren")))
# remove item from list
names.remove("Erez")
print(names)
# drop the last item from list
names.pop()
print(names)
# clear all item from list
names.clear()
print(names)
# find the max number
numbers = [4, 9, 2, 33, 55, 23, 11]
maxi = numbers[0]
for number in numbers:
    if number > maxi:
        maxi = number
print(maxi)

# 2 dimension list or array

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][0])
print(matrix[1][2])

# nested loop with 2 dimension list
for row in matrix:
    for item in row:
        print(item)
