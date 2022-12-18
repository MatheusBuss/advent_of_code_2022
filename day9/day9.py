file = open('rope.txt', 'r')

input = [line.split() for line in file]

steps = [direction*int(times) for direction, times in input]
steps = ''.join(steps)

starting_position = [0, 0]

head = starting_position.copy()
tail = starting_position.copy()
visited = [starting_position.copy()]

directions = {
    'U': [0, 1],
    'D': [0, -1],
    'L': [-1, 0],
    'R': [1, 0]
}


def sign(num):
    if num >= 0:
        return 1
    else:
        return -1


for step in steps:
    head = list(map(int.__add__, head, directions[step]))
    x = head[0] - tail[0]
    y = head[1] - tail[1]
    if abs(x) > 1:
        tail[0] += sign(x)
        if abs(y) > 0:
            tail[1] += y
    if abs(y) > 1:
        tail[1] += sign(y)
        if abs(x) > 0:
            tail[0] += x
    if tail not in visited:
        visited.append(tail.copy())

print(f'Unique tiles visited: {len(visited)}')

num_knots = 9

knots = [starting_position.copy() for _ in range(num_knots + 1)]
visited = [starting_position.copy()]

for step in steps:
    knots[0] = list(map(int.__add__, knots[0], directions[step]))
    for i in range(1, len(knots)):
        x = knots[i-1][0] - knots[i][0]
        y = knots[i-1][1] - knots[i][1]
        if abs(x) > 1:
            knots[i][0] += sign(x)
            if abs(y) > 0:
                knots[i][1] += sign(y)
        elif abs(y) > 1:
            knots[i][1] += sign(y)
            if abs(x) > 0:
                knots[i][0] += sign(x)
    if knots[-1] not in visited:
        visited.append(knots[-1].copy())

print(f'Unique many tiles visited: {len(visited)}')
