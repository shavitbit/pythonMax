import random
import datetime
# implementation of random
rand_num=int(random.random()*100)
print(rand_num)

# choose random from list
members = ['oren', 'tomer', "omer"]
leader = random.choice(members)
print(leader)

print(datetime.date.today())

today = datetime.date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)
