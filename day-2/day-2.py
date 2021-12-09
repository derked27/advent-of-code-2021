import os

filename = "input.txt"
distance = 0
depth = 0

with open(os.path.join(os.path.dirname(__file__), filename), "r") as file:
    for line in file:
        splitInput = line.split(' ')
        direction = splitInput[0]
        amount = int(splitInput[1])

        if direction == "up":
            depth -= amount
        elif direction == "down":
            depth += amount
        elif direction == "forward":
            distance += amount

print(distance * depth)