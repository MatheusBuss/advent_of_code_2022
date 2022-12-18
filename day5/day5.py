file = open('crates.txt', 'r')

lines = [line.rstrip('\n') for line in file]

highest_pile = 8
num_piles = 9

crates = lines[:highest_pile]

instructions = lines[highest_pile+2:]
instructions = [(int(line.split()[1]), int(line.split()[3]),
                 int(line.split()[5])) for line in instructions]

starting_stacks = [None for _ in range(num_piles)]

for i in range(num_piles):
    starting_stacks[i] = [crate[(4*i)+1]
                          for crate in crates if crate[(4*i)+1] != ' ']

stacks = starting_stacks.copy()

for mo, fr, to in instructions:
    moving = stacks[fr-1][:mo]
    moving.reverse()
    stacks[to-1] = moving + stacks[to-1]
    stacks[fr-1] = stacks[fr-1][mo:]

top = ''

for stack in stacks:
    top += stack[0]

print(f'Crates on top: {top}')

new_stacks = starting_stacks.copy()

for mo, fr, to in instructions:
    moving = new_stacks[fr-1][:mo]
    new_stacks[to-1] = moving + new_stacks[to-1]
    new_stacks[fr-1] = new_stacks[fr-1][mo:]

new_top = ''

for stack in new_stacks:
    new_top += stack[0]

print(f'New crates on new top: {new_top}')
