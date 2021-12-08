import os

filename = "input.txt"
counter = 0
currentNumberGroup = []

with open(os.path.join(os.path.dirname(__file__), filename), "r") as file:
    for line in file:
        currentNumber = int(line)
        previousSum = sum(currentNumberGroup)
        currentNumberGroup.append(currentNumber)
        if (len(currentNumberGroup) == 4):
            currentNumberGroup.pop(0)
            currentSum = sum(currentNumberGroup)
            if (currentSum > previousSum):
                counter += 1


print(counter)