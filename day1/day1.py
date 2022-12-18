file = open('calories_input.txt')

values = [line for line in file]

num_elves = 0

for value in values:
    if value == '\n':
        num_elves += 1

elves = [[] for _ in range(num_elves)]

i = 0
for value in values:
    if value != '\n':
        elves[i].append(int(value))
    else:
        i += 1

totals = [sum(elf) for elf in elves]

print('Elf carrying the most: ' + str(max(totals)))

sorted_total = totals

sorted_total.sort(reverse=True)

print(f'First elf: {sorted_total[0]}\nSecond elf: {sorted_total[1]}\nThird elf: {sorted_total[2]}\nThree total: {sum(sorted_total[:3])}')
