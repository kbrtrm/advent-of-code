import re

# Import the file
file_path = "input/03.txt"
with open(file_path, "r") as file:
    data = file.read()

# Regular expression to find valid mul(X,Y) instructions
pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"

# Find all matches in the data
matches = re.findall(pattern, data)

# Calculate the sum of the results of the multiplications
total_sum = sum(int(x) * int(y) for x, y in matches)

# Regular expression to find valid mul(X,Y) instructions with additional spaces or characters
pattern_mul = r"mul\(\s*(\d{1,3})\s*[^0-9]*\s*(\d{1,3})\s*\)"
pattern_do = r"do\(\)"
pattern_dont = r"don't\(\)"

# Initialize variables
total_sum_do = 0
last_seen_do = True

# Iterate through the data
for match in re.finditer(r"do\(\)|don't\(\)|mul\(\s*(\d{1,3})\s*[^0-9]*\s*(\d{1,3})\s*\)", data):
    if match.group() == "do()":
        last_seen_do = True
    elif match.group() == "don't()":
        last_seen_do = False
    else:
        if last_seen_do:
            x, y = re.findall(r"\d{1,3}", match.group())
            total_sum_do += int(x) * int(y)

print(total_sum)
print(total_sum_do)