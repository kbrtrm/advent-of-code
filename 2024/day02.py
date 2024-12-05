import numpy as np

## Part 1

# Import the file
file_path = "input/02.txt"
with open(file_path, "r") as file:
    data = file.read()

# Parse the file
lines = data.split("\n")
# Process the lines further if needed

# Function to check if all numbers are either increasing or decreasing
def check_order(numbers):
    increasing = all(numbers[i] < numbers[i+1] for i in range(len(numbers)-1))
    decreasing = all(numbers[i] > numbers[i+1] for i in range(len(numbers)-1))
    return increasing or decreasing

valid_items = []
for item in lines:
    numbers = list(map(int, item.split()))
    if not check_order(numbers):
        continue
    if not all(abs(numbers[i] - numbers[i+1]) in [1, 2, 3] for i in range(len(numbers)-1)):
        continue
    valid_items.append(item)

print(len(valid_items))

## part 2


import numpy as np

# Function to check if all numbers are either increasing or decreasing, considering the Problem Dampener rule
def check_dampened_order(numbers):
    diff = np.diff(numbers)
    increasing = np.all(diff > 0) and np.all(diff <= 3)
    decreasing = np.all(diff < 0) and np.all(diff >= -3)
    if increasing or decreasing:
        return True
    for i in range(len(numbers)-1):
        if abs(numbers[i] - numbers[i+1]) >= 1 and abs(numbers[i] - numbers[i+1]) <= 3:
            # Remove the current number and check if the remaining numbers satisfy the order condition
            if check_dampened_order(numbers[:i] + numbers[i+1:]):
                return True
    return False

valid_items_d = []
for item in lines:
    numbers = list(map(int, item.split()))
    if not check_dampened_order(numbers):
        continue
    valid_items_d.append(item)

print(len(valid_items_d))
