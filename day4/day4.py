import fileinput
file = open('assignments.txt', 'r')


def contains(in1: int, out1: int, in2: int, out2: int) -> bool:
    if (in1 <= in2 and out1 >= out2) or (in2 <= in1 and out2 >= out1):
        return True
    else:
        return False


def decode_line(shifts: str) -> tuple:
    first, second = shifts.strip().split(',')
    in1, out1 = first.split('-')
    in2, out2 = second.split('-')
    return (int(in1), int(out1), int(in2), int(out2))


assignments = [decode_line(line) for line in file]


containment = [contains(in1, out1, in2, out2)
               for in1, out1, in2, out2 in assignments]

print(f'How many pairs are conatined: {sum(containment)}')


def overlaps(in1: int, out1: int, in2: int, out2: int) -> bool:
    if (in1 <= in2 and out1 >= in2) or (in2 <= in1 and out2 >= in1):
        return True
    else:
        return False


overlaping = [overlaps(in1, out1, in2, out2)
              for in1, out1, in2, out2 in assignments]

print(f'How many pairs overlap: {sum(overlaping)}')
