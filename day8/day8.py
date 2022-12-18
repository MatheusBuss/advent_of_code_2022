file = open('trees.txt', 'r')

lines = [line.strip() for line in file]

grid = [None for _ in range(len(lines))]
round = [None for _ in range(len(lines))]
north = [None for _ in range(len(lines))]
south = [None for _ in range(len(lines))]
west = [None for _ in range(len(lines))]
east = [None for _ in range(len(lines))]
visibility = [None for _ in range(len(lines))]
results = [None for _ in range(len(lines))]

for i in range(len(grid)):
    grid[i] = [int(char) for char in lines[i]]
    north[i] = [False for _ in lines[i]]
    south[i] = [False for _ in lines[i]]
    west[i] = [False for _ in lines[i]]
    east[i] = [False for _ in lines[i]]
    visibility[i] = [False for _ in lines[i]]
    results[i] = [False for _ in lines[i]]

rows = len(grid)
columns = len(grid[0])


def check_visibility(grid, i, j, direction, tallest):
    if grid[i][j] > tallest:
        tallest = grid[i][j]
        direction[i][j] = True
    return direction, tallest


for j in range(1, columns-1):
    tallest = -1
    for i in range(rows-1):
        north, tallest = check_visibility(grid, i, j, north, tallest)

for j in range(1, columns-1):
    tallest = -1
    for i in range(rows-1, 0, -1):
        south, tallest = check_visibility(grid, i, j, south, tallest)

for i in range(1, rows-1):
    tallest = -1
    for j in range(columns-1):
        west, tallest = check_visibility(grid, i, j, west, tallest)

for i in range(1, rows-1):
    tallest = -1
    for j in range(columns-1, 0, -1):
        east, tallest = check_visibility(grid, i, j, east, tallest)

counter = 0
for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows-1:
            visibility[i][j] = True
            counter += 1
        elif j == 0 or j == columns-1:
            visibility[i][j] = True
            counter += 1
        elif north[i][j] or south[i][j] or west[i][j] or east[i][j]:
            visibility[i][j] = True
            counter += 1

print(f'Visible trees: {counter}')


def check_north(start, column, height):
    i = 0
    for i in range(start-1, -1, -1):
        if grid[i][column] >= height:
            break
    return start - i


def check_south(start, column, height):
    i = start
    for i in range(start+1, len(grid)):
        if grid[i][column] >= height:
            break
    return i - start


def check_west(row, start, height):
    j = 0
    for j in range(start-1, -1, -1):
        if grid[row][j] >= height:
            break
    return start - j


def check_east(row, start, height):
    j = start
    for j in range(start+1, len(grid[row])):
        if grid[row][j] >= height:
            break
    return j - start


viewtiful = 0
for i in range(rows):
    for j in range(columns):
        north = check_north(i, j, grid[i][j])
        south = check_south(i, j, grid[i][j])
        west = check_west(i, j, grid[i][j])
        east = check_east(i, j, grid[i][j])
        result = north * south * west * east
        viewtiful = max(viewtiful, result)
        results[i][j] = result

print(f'Greatest scenic score: {str(viewtiful)}')
