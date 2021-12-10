import os

filename = "input.txt"
line_count = 0
report_summary_one_found = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open(os.path.join(os.path.dirname(__file__), filename), "r") as file:
    for line in file:
        line_count += 1
        for i, v in enumerate(line):
            if (v == "1"):
                report_summary_one_found[i] += 1

gamma_rate = ""
epsilon_rate = ""

for count in report_summary_one_found:
    off_count = line_count - count
    if count > off_count:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

number_gamma_rate = int(gamma_rate, 2)
number_epsilon_rate = int(epsilon_rate, 2)
print(number_gamma_rate * number_epsilon_rate)