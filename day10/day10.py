file = open('instructions.txt', 'r')

# file = [
#     'addx 15',
#     'addx -11',
#     'addx 6',
#     'addx -3',
#     'addx 5',
#     'addx -1',
#     'addx -8',
#     'addx 13',
#     'addx 4',
#     'noop',
#     'addx -1',
#     'addx 5',
#     'addx -1',
#     'addx 5',
#     'addx -1',
#     'addx 5',
#     'addx -1',
#     'addx 5',
#     'addx -1',
#     'addx -35',
#     'addx 1',
#     'addx 24',
#     'addx -19',
#     'addx 1',
#     'addx 16',
#     'addx -11',
#     'noop',
#     'noop',
#     'addx 21',
#     'addx -15',
#     'noop',
#     'noop',
#     'addx -3',
#     'addx 9',
#     'addx 1',
#     'addx -3',
#     'addx 8',
#     'addx 1',
#     'addx 5',
#     'noop',
#     'noop',
#     'noop',
#     'noop',
#     'noop',
#     'addx -36',
#     'noop',
#     'addx 1',
#     'addx 7',
#     'noop',
#     'noop',
#     'noop',
#     'addx 2',
#     'addx 6',
#     'noop',
#     'noop',
#     'noop',
#     'noop',
#     'noop',
#     'addx 1',
#     'noop',
#     'noop',
#     'addx 7',
#     'addx 1',
#     'noop',
#     'addx -13',
#     'addx 13',
#     'addx 7',
#     'noop',
#     'addx 1',
#     'addx -33',
#     'noop',
#     'noop',
#     'noop',
#     'addx 2',
#     'noop',
#     'noop',
#     'noop',
#     'addx 8',
#     'noop',
#     'addx -1',
#     'addx 2',
#     'addx 1',
#     'noop',
#     'addx 17',
#     'addx -9',
#     'addx 1',
#     'addx 1',
#     'addx -3',
#     'addx 11',
#     'noop',
#     'noop',
#     'addx 1',
#     'noop',
#     'addx 1',
#     'noop',
#     'noop',
#     'addx -13',
#     'addx -19',
#     'addx 1',
#     'addx 3',
#     'addx 26',
#     'addx -30',
#     'addx 12',
#     'addx -1',
#     'addx 3',
#     'addx 1',
#     'noop',
#     'noop',
#     'noop',
#     'addx -9',
#     'addx 18',
#     'addx 1',
#     'addx 2',
#     'noop',
#     'noop',
#     'addx 9',
#     'noop',
#     'noop',
#     'noop',
#     'addx -1',
#     'addx 2',
#     'addx -37',
#     'addx 1',
#     'addx 3',
#     'noop',
#     'addx 15',
#     'addx -21',
#     'addx 22',
#     'addx -6',
#     'addx 1',
#     'noop',
#     'addx 2',
#     'addx 1',
#     'noop',
#     'addx -10',
#     'noop',
#     'noop',
#     'addx 20',
#     'addx 1',
#     'addx 2',
#     'addx 2',
#     'addx -6',
#     'addx -11',
#     'noop',
#     'noop',
#     'noop'
# ]

instructions = [line.split() for line in file]

tally = 1

cycles = []
cycles.append(tally)
cycles.append(tally)

for instruction in instructions:
    if len(instruction) > 1:
        cycles.append(tally)
        tally += int(instruction[1])
        cycles.append(tally)
    else:
        cycles.append(tally)

chosen = [20, 60, 100, 140, 180, 220]

total = 0

for i in chosen:
    print(f'{i}: Value:{cycles[i]}, Score: {cycles[i]*i}')
    total += cycles[i]*i

print(f'Total sum: {total}')

lines = [[None for _ in range(40)] for _ in range(int(len(cycles)/40))]

for i, value in enumerate(cycles[1:]):
    position = i % 40
    row = int(i/40)
    try:
        if value >= position - 1 and value <= position + 1:
            lines[row][position] = '#'
        else:
            lines[row][position] = ' '
    except:
        break


for line in lines:
    char = ''
    for letter in line:
        char += letter
    print(char)
