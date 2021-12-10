import os


def get_oxygen_rating(input: list, index: int):
    if len(input) == 1:
        return input[0]
    new_binary_dictionary = {"0": [], "1": []}
    for item in input:
        new_binary_dictionary[item[index]].append(item)
    if len(new_binary_dictionary["1"]) >= len(new_binary_dictionary["0"]):
        return get_oxygen_rating(new_binary_dictionary["1"], index + 1)
    else:
        return get_oxygen_rating(new_binary_dictionary["0"], index + 1)


def get_c02_rating(input: list, index: int):
    if len(input) == 1:
        return input[0]
    new_binary_dictionary = {"0": [], "1": []}
    for item in input:
        new_binary_dictionary[item[index]].append(item)
    if len(new_binary_dictionary["0"]) <= len(new_binary_dictionary["1"]):
        return get_c02_rating(new_binary_dictionary["0"], index + 1)
    else:
        return get_c02_rating(new_binary_dictionary["1"], index + 1)


filename = "input.txt"
binary_dictionary = {"0": [], "1": []}

with open(os.path.join(os.path.dirname(__file__), filename), "r") as file:
    for line in file:
        binary_dictionary[line[0]].append(line)

oxygen_rating_string = (
    get_oxygen_rating(binary_dictionary["0"], 1) if binary_dictionary["1"] >= binary_dictionary["0"]
    else get_oxygen_rating(binary_dictionary["1"], 1)
)

c02_rating_string = (
    get_c02_rating(binary_dictionary["1"], 1) if binary_dictionary["0"] <= binary_dictionary["1"]
    else get_c02_rating(binary_dictionary["0"], 1)
)

oxygen_rating = int(oxygen_rating_string, 2)
c02_rating = int(c02_rating_string, 2)

life_support_rating = oxygen_rating * c02_rating

print(oxygen_rating_string)
print(c02_rating_string)
print(oxygen_rating)
print(c02_rating)

print(life_support_rating)
