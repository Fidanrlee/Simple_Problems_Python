import random,time
numberOfStreaks = 0
R_list = []
for experimentNumber in range(100000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    item = random.choice(['H', 'T'])
    R_list.append(item)


experimentNumber = 0
numberOfStreaks = 0

for experimentNumber in range(100000):
    # Code that checks if there is a streak of 6 heads or tails in a row.
    count = 0
    while experimentNumber < len(R_list) and R_list[experimentNumber] == "H":
        experimentNumber += 1
        count += 1
    if count >= 6:
        numberOfStreaks += 1

    count = 0
    while experimentNumber < len(R_list) and R_list[experimentNumber] == "T":
        experimentNumber += 1
        count += 1
    if count >= 6:
        numberOfStreaks += 1


print('Chance of streak: %s%%' % (numberOfStreaks / 100))