file = open('rucksacks.txt', 'r')

rucksacks = [line.strip() for line in file]


def priority_score(letter: str) -> int:
    if ord(letter) >= 97:
        return ord(letter)-96
    else:
        return ord(letter)-38


def repeat(rucksack: str) -> str:
    first = rucksack[:int(len(rucksack)/2)]
    last = rucksack[int(len(rucksack)/2):]
    for letter in first:
        if letter in last:
            return letter


repeats = [repeat(rucky) for rucky in rucksacks]

priorities = [priority_score(rep) for rep in repeats]

print(f'Total priorities: {sum(priorities)}')


def badge(ruck1: str, ruck2: str, ruck3: str) -> str:
    for letter in ruck1:
        if letter in ruck2 and letter in ruck3:
            return letter


groups = [[rucksacks[i*3], rucksacks[(i*3)+1], rucksacks[(i*3)+2]]
          for i in range(int(len(rucksacks)/3))]

badges = [badge(ruck[0], ruck[1], ruck[2]) for ruck in groups]

badges_priorities = [priority_score(group) for group in badges]

print(f'Total badges priorities: {sum(badges_priorities)}')
