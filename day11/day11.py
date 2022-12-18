file = open('monkey_donkey.txt', 'r')

managed = True

mmc = 0


class Monkey():
    def __init__(self, items: list, operation, num_test: int, true_monkey, false_monkey) -> None:
        self.items = items
        self.operation = operation
        self.num_test = num_test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspected = 0

    def turn(self):
        for item in self.items:
            worry = self._inspect(item)
            self.inspected += 1
            if self._test_item(worry):
                self.true_monkey.items.append(worry)
            else:
                self.false_monkey.items.append(worry)
        self.items = []

    def _test_item(self, num):
        if num % self.num_test == 0:
            return True
        else:
            return False

    def _inspect(self, item_value):
        value = self.operation(item_value)
        if managed:
            return int(value/3)
        else:
            return int(value % mmc)


initial_state = [
    (
        [57, 58],
        lambda x: x * 19,
        7,
        2,
        3
    ),
    (
        [66, 52, 59, 79, 94, 73],
        lambda x: x + 1,
        19,
        4,
        6
    ),
    (
        [80],
        lambda x: x + 6,
        5,
        7,
        5
    ),
    (
        [82, 81, 68, 66, 71, 83, 75, 97],
        lambda x: x + 5,
        11,
        5,
        2
    ),
    (
        [55, 52, 67, 70, 69, 94, 90],
        lambda x: x * x,
        17,
        0,
        3
    ),
    (
        [69, 85, 89, 91],
        lambda x: x + 7,
        13,
        1,
        7
    ),
    (
        [75, 53, 73, 52, 75],
        lambda x: x * 7,
        2,
        0,
        4
    ),
    (
        [94, 60, 79],
        lambda x: x + 2,
        3,
        1,
        6
    )
]


def start_monkeys(initial_state):
    monkeys = [
        Monkey(
            monkey[0],
            monkey[1],
            monkey[2],
            monkey[3],
            monkey[4]
        ) for monkey in initial_state]

    for monkey in monkeys:
        monkey.true_monkey = monkeys[monkey.true_monkey]
        monkey.false_monkey = monkeys[monkey.false_monkey]

    return monkeys


monkeys = start_monkeys(initial_state)

num_tests = 20

for turn in range(num_tests):
    for monkey in monkeys:
        monkey.turn()

activity = []

for i, monkey in enumerate(monkeys):
    activity.append(monkey.inspected)
    print(f'{i} - Inspected {monkey.inspected} items')

activity.sort()

item1, item2 = activity[-2:]
print(f'score: {item1*item2}')

initial_state = [
    (
        [57, 58],
        lambda x: x * 19,
        7,
        2,
        3
    ),
    (
        [66, 52, 59, 79, 94, 73],
        lambda x: x + 1,
        19,
        4,
        6
    ),
    (
        [80],
        lambda x: x + 6,
        5,
        7,
        5
    ),
    (
        [82, 81, 68, 66, 71, 83, 75, 97],
        lambda x: x + 5,
        11,
        5,
        2
    ),
    (
        [55, 52, 67, 70, 69, 94, 90],
        lambda x: x * x,
        17,
        0,
        3
    ),
    (
        [69, 85, 89, 91],
        lambda x: x + 7,
        13,
        1,
        7
    ),
    (
        [75, 53, 73, 52, 75],
        lambda x: x * 7,
        2,
        0,
        4
    ),
    (
        [94, 60, 79],
        lambda x: x + 2,
        3,
        1,
        6
    )
]

monkeys = start_monkeys(initial_state)

divisors = [monkey.num_test for monkey in monkeys]

i = 0
j = max(divisors)
while True:
    i += 1
    test = [((j*i) % div) for div in divisors]
    if sum(test) == 0:
        break

mmc = i * j

managed = False

num_tests = 10_000

for turn in range(num_tests):
    for monkey in monkeys:
        monkey.turn()

activity = []

for i, monkey in enumerate(monkeys):
    activity.append(monkey.inspected)
    print(f'{i} - Inspected {monkey.inspected} items')

activity.sort()
item1, item2 = activity[-2:]
print(f'Final score: {item1*item2}')
