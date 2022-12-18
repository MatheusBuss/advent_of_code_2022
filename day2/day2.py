file = open('rock_paper_scissor.txt', 'r')

win = 6
tie = 3
los = 0

rock = 1
paper = 2
scissor = 3

results = [
    [tie, win, los],
    [los, tie, win],
    [win, los, tie]
]


def translate(entry: str) -> int:
    if entry == 'A' or entry == 'X':
        return rock
    elif entry == 'B' or entry == 'Y':
        return paper
    else:
        return scissor


plays = [line.split() for line in file]

scores = [results[translate(entry[0])-1][translate(entry[1])-1] +
          translate(entry[1]) for entry in plays[:-1]]

print(f'Total score: {sum(scores)}')

new_results = [
    [scissor, rock, paper],
    [rock, paper, scissor],
    [paper, scissor, rock]
]


def new_translate(entry: str) -> int:
    if entry == 'X':
        return los
    elif entry == 'Y':
        return tie
    else:
        return win


new_scores = [new_results[translate(entry[0])-1][translate(entry[1])-1] +
              new_translate(entry[1]) for entry in plays[:-1]]

print(f'Total new score: {sum(new_scores)}')
