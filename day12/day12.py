from datetime import datetime

import time
import os

start_time = datetime.now()

file = open('landscape.txt', 'r')

lines = [line.strip() for line in file]

terrain = []

start_height = ord('a')
end_height = ord('z')

for line in lines:
    terrain.append([ord(char)-start_height for char in line])

grid_height = len(terrain)
grid_width = len(terrain[0])

steps = [[-1 for _ in terrain[0]] for _ in terrain]

start = 'S'
end = 'E'

for i in range(len(terrain)):
    for j in range(len(terrain[i])):
        if isinstance(start, str) and terrain[i][j] == ord(start)-start_height:
            start = (i, j)
            terrain[i][j] = 0
        elif isinstance(end, str) and terrain[i][j] == ord(end)-start_height:
            end = (i, j)
            terrain[i][j] = end_height-start_height


def is_valid(current_height, dest, grid, steps):
    dest_height = grid[dest[0]][dest[1]]
    if dest_height <= current_height + 1 and steps[dest[0]][dest[1]] == -1:
        return True
    else:
        return False


def find_next(i, j, grid, steps):
    height = grid[i][j]
    new_visits = []
    # North
    if i > 0 and is_valid(height, (i-1, j), grid, steps):
        steps[i-1][j] = steps[i][j]+1
        new_visits.append((i-1, j))
    # East
    if j < grid_width-1 and is_valid(height, (i, j+1), grid, steps):
        steps[i][j+1] = steps[i][j]+1
        new_visits.append((i, j+1))
    # South
    if i < grid_height-1 and is_valid(height, (i+1, j), grid, steps):
        steps[i+1][j] = steps[i][j]+1
        new_visits.append((i+1, j))
    # West
    if j > 0 and is_valid(height, (i, j-1), grid, steps):
        steps[i][j-1] = steps[i][j]+1
        new_visits.append((i, j-1))
    return new_visits


steps[start[0]][start[1]] = 0

visits = [(start[0], start[1])]

max_value = 370

while visits != []:
    next = visits[0]
    visits += find_next(next[0], next[1], terrain, steps)
    visits = visits[1:]
    string = ''
    for i in range(len(steps)):
        for j in range(len(steps[0])):
            disp_number = str(
                terrain[i][j]) if terrain[i][j] >= 10 else '0' + str(terrain[i][j])
            terrain_color = 55 + int((200/26)*terrain[i][j])
            if steps[i][j] != -1:
                color_value = int((steps[i][j]/max_value) * 255)
                string += f'\033[38;2;{color_value};{255 - color_value};0m{disp_number}\033[0m' + ' '
            else:
                string += f'\033[38;2;{terrain_color};{terrain_color};{terrain_color}m{disp_number}\033[0m' + ' '
        string += '\n'
    os.system('clear')
    print(string)
    time.sleep(0.01)

print(steps[end[0]][end[1]])

num_steps = steps[end[0]][end[1]]

current = end
path = [end]
for k in range(num_steps):
    current_step = steps[current[0]][current[1]]
    current_height = terrain[current[0]][current[1]]
    current_row = current[0]
    current_column = current[1]
    if current_column < grid_width - 1 and steps[current_row][current_column+1] == current_step - 1 and terrain[current_row][current_column+1] >= current_height - 1:
        current = (current_row, current_column+1)
    elif current_row < grid_height - 1 and steps[current_row+1][current_column] == current_step - 1 and terrain[current_row + 1][current_column] >= current_height - 1:
        current = (current_row+1, current_column)
    elif current_column > 0 and steps[current_row][current_column-1] == current_step - 1 and terrain[current_row][current_column - 1] >= current_height - 1:
        current = (current_row, current_column-1)
    else:
        current = (current[0]-1, current[1])
    path.append(current)
    string = ''
    for i in range(len(steps)):
        # break
        for j in range(len(steps[0])):
            disp_number = str(
                terrain[i][j]) if terrain[i][j] >= 10 else '0' + str(terrain[i][j])
            terrain_color = 55 + int((200/26)*terrain[i][j])
            if (i, j) in path:
                string += f'\033[38;2;255;215;0m{disp_number}\033[0m' + ' '
            elif steps[i][j] != -1:
                color_value = int((steps[i][j]/max_value) * 255)
                string += f'\033[38;2;{color_value};{255 - color_value};0m{disp_number}\033[0m' + ' '
            else:
                string += f'\033[38;2;{terrain_color};{terrain_color};{terrain_color}m{disp_number}\033[0m' + ' '
        string += '\n'
    os.system('clear')
    print(string)
    time.sleep(0.02)

# print(path)
# print(current)

inverted_terrain = []

for line in lines:
    inverted_terrain.append([end_height - ord(char) for char in line])

inverted_terrain[end[0]][end[1]] = 0
inverted_terrain[start[0]][start[1]] = end_height-start_height

inverted_steps = [[-1 for _ in inverted_terrain[0]] for _ in inverted_terrain]

inverted_steps[end[0]][end[1]] = 0

inverted_visits = [(end[0], end[1])]

while inverted_visits != []:
    next = inverted_visits[0]
    inverted_visits += find_next(next[0], next[1],
                                 inverted_terrain, inverted_steps)
    inverted_visits = inverted_visits[1:]

candidates = []

for i in range(len(inverted_terrain)):
    for j in range(len(inverted_terrain[0])):
        if inverted_terrain[i][j] == end_height-start_height:
            candidates.append(inverted_steps[i][j])

min_steps = max(candidates)
for candidate in candidates:
    if candidate != -1 and candidate < min_steps:
        min_steps = candidate

print(min_steps)

end_time = datetime.now()

duration = end_time - start_time

print(duration.total_seconds())
