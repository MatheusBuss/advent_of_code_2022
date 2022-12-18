from datetime import datetime, timedelta
file = open('sensors.txt', 'r')


lines = [line for line in file]

# lines = [
#     'Sensor at x=2, y=18: closest beacon is at x=-2, y=15',
#     'Sensor at x=9, y=16: closest beacon is at x=10, y=16',
#     'Sensor at x=13, y=2: closest beacon is at x=15, y=3',
#     'Sensor at x=12, y=14: closest beacon is at x=10, y=16',
#     'Sensor at x=10, y=20: closest beacon is at x=10, y=16',
#     'Sensor at x=14, y=17: closest beacon is at x=10, y=16',
#     'Sensor at x=8, y=7: closest beacon is at x=2, y=10',
#     'Sensor at x=2, y=0: closest beacon is at x=2, y=10',
#     'Sensor at x=0, y=11: closest beacon is at x=2, y=10',
#     'Sensor at x=20, y=14: closest beacon is at x=25, y=17',
#     'Sensor at x=17, y=20: closest beacon is at x=21, y=22',
#     'Sensor at x=16, y=7: closest beacon is at x=15, y=3',
#     'Sensor at x=14, y=3: closest beacon is at x=15, y=3',
#     'Sensor at x=20, y=1: closest beacon is at x=15, y=3'
# ]

sensors = []
beacons = []

for line in lines:
    line = line.strip().split()
    sensor_x = int(line[2].strip('x=').strip(','))
    sensor_y = int(line[3].strip('y=').strip(':'))
    beacon_x = int(line[8].strip('x=').strip(','))
    beacon_y = int(line[9].strip('y='))
    dist_x = abs(sensor_x - beacon_x)
    dist_y = abs(sensor_y - beacon_y)
    dist = dist_x + dist_y
    sensors.append((sensor_x, sensor_y, dist))
    beacons.append((beacon_x, beacon_y))


def row_occupations(test_row, beacons, sensors, lower_x=None, upper_x=None):

    occupations = []

    for x, y, dist in sensors:
        row_dist = abs(y - test_row)
        if row_dist > dist:
            continue
        start_x = x - abs(dist - row_dist)
        end_x = x + abs(dist - row_dist)

        occupations.append((start_x, end_x))

    occupations.sort()

    filtered_occupations = []

    start = None

    for occupation in occupations:
        flag = False
        if start == None:
            if lower_x:
                if occupation[1] < lower_x:
                    continue
                start = min(occupation[0], lower_x)
            else:
                start = occupation[0]
            if upper_x:
                if occupation[0] >= upper_x:
                    start = upper_x
                    cur_max = upper_x
                    break
                elif occupation[1] >= upper_x:
                    cur_max = upper_x
                    break
                else:
                    cur_max = occupation[1]
            else:
                cur_max = occupation[1]
            continue
        if occupation[0] <= cur_max + 1:
            cur_max = max(cur_max, occupation[1])
        else:
            filtered_occupations.append(range(start, cur_max + 1))
            start = None
            flag = True

    if flag:
        latest = sorted(occupations)[-1]
        filtered_occupations.append(range(latest[0], latest[1] + 1))
    else:
        filtered_occupations.append(range(start, cur_max + 1))

    return filtered_occupations


test_row = 2000000

# test_row = 10

temp_set = set()

test_occupation = temp_set.union(*row_occupations(test_row, beacons, sensors))

for x, y, _ in sensors:
    if y == test_row and x in test_occupation:
        test_occupation.remove(x)

for x, y in beacons:
    if y == test_row and x in test_occupation:
        test_occupation.remove(x)

print(len(test_occupation))


start_time = datetime.now()

min_coord = 0
max_coord = 4_000_000
# max_coord = 20

for i in range(max_coord):
    occupations = row_occupations(i, beacons, sensors, min_coord, max_coord)
    if len(occupations) > 1:
        y = i
        break

x = [*occupations[0]][-1] + 1

print(f'{x=},{y=}, frequency: {(x*4000000) + y}')

print(f'Took {datetime.now() - start_time}')
