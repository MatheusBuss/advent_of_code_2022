file = open('valves.txt', 'r')

lines = [line for line in file]

# lines = [
# 'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB',
# 'Valve BB has flow rate=13; tunnels lead to valves CC, AA',
# 'Valve CC has flow rate=2; tunnels lead to valves DD, BB',
# 'Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE',
# 'Valve EE has flow rate=3; tunnels lead to valves FF, DD',
# 'Valve FF has flow rate=0; tunnels lead to valves EE, GG',
# 'Valve GG has flow rate=0; tunnels lead to valves FF, HH',
# 'Valve HH has flow rate=22; tunnel leads to valve GG',
# 'Valve II has flow rate=0; tunnels lead to valves AA, JJ',
# 'Valve JJ has flow rate=21; tunnel leads to valve II'
# ]

nodes = {}
for line in lines:
    line = line.replace(',', '').replace(';', '').split()
    node = line[1]
    nodes[node] = {
        'rate': int(line[4].split('=')[-1]),
        'connections': tuple(line[9:]),
        'distances': None
    }

transport = 1
valve_time = 1


def calculate_distances(origin: str, nodes: dict):
    dist = 0
    distances = {origin: dist}
    queue = list(nodes[origin]['connections'])
    while queue != []:
        queue_len = len(queue)
        dist += 1
        for i in range(queue_len):
            node = queue[i]
            distances[node] = dist
            for connection in nodes[node]['connections']:
                if connection not in distances and connection not in queue:
                    queue.append(connection)
        queue = queue[queue_len:]
    return distances


non_empty = set(node for node in nodes if nodes[node]['rate'])


def step(location: str, time_remaining: int, visited: set, stack: list, score: int):
    distances = calculate_distances(location, nodes)
    valid_distances = tuple((node, distance) for node, distance in distances.items() if
                            node in non_empty and distance + valve_time <= time_remaining and node not in visited)
    for node, distance in valid_distances:
        time_taken = distance + valve_time
        total_score = score + (nodes[node]['rate']
                               * (time_remaining - time_taken))
        stack.append((visited.union({node}), node,
                     time_remaining - time_taken, total_score))


def volcano(stack):
    max_score = stack[-1][-1]
    while stack != []:
        visited, location, time_remaining, score = stack[-1]
        if score > max_score:
            max_score = score
            max_visited = visited
        current_stack = len(stack)
        step(location, time_remaining, visited, stack, score)
        stack.pop(current_stack - 1)
    return max_score, max_visited


start_location = 'AA'
start_duration = 30
start_score = 0
stack = [({start_location}, start_location, start_duration, start_score)]

print(f'Alone: {volcano(stack)}')

start_location = 'AA'
start_duration = 26
start_score = 0
stack = [({start_location}, start_location, start_duration, start_score)]

first_score, first_visited = volcano(stack)

stack = [(first_visited, start_location, start_duration, first_score)]

print(f'With Ellie boy: {volcano(stack)}')
