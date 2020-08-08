# while loops
print("while loop:\n")
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")

# game of while loop
guess_count = 0
guess_limit = 3
secret_num = 5
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_num:
        print("you win")
        break
else:
    print("you failed")

# for loop
for item in 'Devops':
    print(item)

arr1 = ["oren","erez","meggie","tal","shlomi"]
for item in arr1:
    print(item)

for item in range(5):
    print("im item number " + str(item))

arr2 = [10,20,30]
total = 0
for i in arr2:
    total = total + i
print(str(total))

# nested loop
for x in range(4):
    for y in range(3):
        print(f'({x} , {y})')