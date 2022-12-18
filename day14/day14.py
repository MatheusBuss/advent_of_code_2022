file = open('rocks.txt', 'r')

lines = [line.strip().split(' -> ') for line in file]

occupied = []

for line in lines:
    for i in range(len(line)):
        if i + 1 < len(line):
            start_x = int(line[i].split(',')[0])
            end_x = int(line[i+1].split(',')[0])
            start_y = int(line[i].split(',')[1])
            end_y = int(line[i+1].split(',')[1])
            if start_x != end_x:
                for j in range(min(start_x, end_x), max(start_x, end_x)+1):
                    occupied.append((j, start_y))
            else:
                for j in range(min(start_y, end_y), max(start_y, end_y)+1):
                    occupied.append((start_x, j))

ys = [coord[1] for coord in occupied]
max_y = max(ys)

occupied = set(occupied)


def cycle(sand, bottom=999):
    current_x = sand[0]
    current_y = sand[1]
    if current_y + 1 == bottom:
        return False
    elif (current_x, current_y + 1) not in occupied:
        return (current_x, current_y + 1)
    elif (current_x - 1, current_y + 1) not in occupied:
        return (current_x - 1, current_y + 1)
    elif (current_x + 1, current_y + 1) not in occupied:
        return (current_x + 1, current_y + 1)
    else:
        return False


init_sand = (500, 0)


sand = (init_sand[0], init_sand[1])

counter = 0


while sand[1] < max_y:
    movement = cycle(sand)
    if movement:
        sand = movement
    else:
        counter += 1
        occupied.add(sand)
        sand = (init_sand[0], init_sand[1])

print(f'Grains to bottom: {counter}')

while (500, 0) not in occupied:
    movement = cycle(sand, max_y+2)
    if movement:
        sand = movement
    else:
        counter += 1
        occupied.add(sand)
        sand = (init_sand[0], init_sand[1])

print(f'Grains to top: {counter}')
