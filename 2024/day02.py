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

## gave up on part 2, will come back to it later