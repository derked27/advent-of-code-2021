import os

filename = "input.txt"
lastNumber = 10000
counter = 0

with open(os.path.join(os.path.dirname(__file__), filename), "r") as file:
    for line in file:
        currentNumber = int(line)
        if (currentNumber > lastNumber):
            counter += 1
        lastNumber = currentNumber
print(counter)