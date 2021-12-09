import os

filename = "input.txt"
distance = 0
depth = 0
aim = 0

with open(os.path.join(os.path.dirname(__file__), filename), "r") as file:
    for line in file:
        splitInput = line.split(' ')
        direction = splitInput[0]
        amount = int(splitInput[1])

        if direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount
        elif direction == "forward":
            distance += amount
            depth += aim * amount

print(distance * depth)