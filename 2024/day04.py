# Import the file
file_path = "input/04.txt"
with open(file_path, "r") as file:
    data = file.read().splitlines()

# Convert the input data into a 2D array
grid = [list(line) for line in data]

def search_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1),  # right, down, down-right, down-left
        (0, -1), (-1, 0), (-1, -1), (-1, 1)  # left, up, up-left, up-right
    ]
    occurrences = []

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                found = True
                for k in range(word_len):
                    nr, nc = r + k * dr, c + k * dc
                    if not is_valid(nr, nc) or grid[nr][nc] != word[k]:
                        found = False
                        break
                if found:
                    occurrences.append((r, c, dr, dc))

    return occurrences

# Find all occurrences of "XMAS"
word = "XMAS"
occurrences = search_word(grid, word)

# Print the count of occurences
print(len(occurrences))

def search_mas_x_pattern(grid):
    rows, cols = len(grid), len(grid[0])
    pattern_positions = []

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_pattern(r, c):
        # Define all four possible "MAS" X patterns
        patterns = [
            [(r, c), (r, c + 2), (r + 1, c + 1), (r + 2, c), (r + 2, c + 2)],  # M.S .A. M.S
            [(r, c), (r, c + 2), (r + 1, c + 1), (r + 2, c), (r + 2, c + 2)],  # S.S .A. M.M
            [(r, c), (r, c + 2), (r + 1, c + 1), (r + 2, c), (r + 2, c + 2)],  # M.M .A. S.S
            [(r, c), (r, c + 2), (r + 1, c + 1), (r + 2, c), (r + 2, c + 2)]   # S.M .A. S.M
        ]
        chars = [
            ['M', 'S', 'A', 'M', 'S'],
            ['S', 'S', 'A', 'M', 'M'],
            ['M', 'M', 'A', 'S', 'S'],
            ['S', 'M', 'A', 'S', 'M']
        ]

        for pattern, char_set in zip(patterns, chars):
            found = True
            for (x, y), char in zip(pattern, char_set):
                if not is_valid(x, y) or grid[x][y] != char:
                    found = False
                    break
            if found:
                return True
        return False

    for r in range(rows - 2):
        for c in range(cols - 2):
            if check_pattern(r, c):
                pattern_positions.append((r, c))

    return pattern_positions

# Find all occurrences of the "MAS" X pattern
mas_x_occurrences = search_mas_x_pattern(grid)

# Print the count of occurrences
print(len(mas_x_occurrences))