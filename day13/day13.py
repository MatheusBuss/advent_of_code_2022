file = open('signals.txt', 'r')


lines = file.readlines()


def recursion_parsing(start, string):
    i = start
    result = []
    while string[i] != ']':
        if string[i] == '[':
            i, returned = recursion_parsing(i + 1, string)
            result.append(returned)
            i += 1
        elif string[i] == ',':
            i += 1
        else:
            number = ''
            while string[i].isdigit():
                number += string[i]
                i += 1
            result.append(int(number))
    return i, result


signals = [(recursion_parsing(1, lines[i*3].strip())[1], recursion_parsing(1, lines[(i*3) + 1].strip())[1])
           for i in range(int(len(lines)/3) + 1)]


def compare_signal(signals1, signals2):
    if len(signals1) == 0:
        return 1
    if len(signals2) == 0:
        return -1
    for i in range(min(len(signals1), len(signals2))):
        if isinstance(signals1[i], list):
            if isinstance(signals2[i], list):
                test = compare_signal(signals1[i], signals2[i])
            else:
                test = compare_signal(signals1[i], [signals2[i]])
            if test:
                return test
        elif isinstance(signals2[i], list):
            test = compare_signal([signals1[i]], signals2[i])
            if test:
                return test
        elif signals1[i] < signals2[i]:
            return 1
        elif signals1[i] > signals2[i]:
            return -1
    if len(signals1) < len(signals2):
        return 1
    elif len(signals1) > len(signals2):
        return -1
    else:
        return 0


results = []

for signal in signals:
    order = compare_signal(signal[0], signal[1])
    results.append(order)

total = 0

for i in range(len(results)):
    if results[i] == 1:
        total += (i + 1)
print(total)

additional_packets = [[[2]], [[6]]]
packets = [packet for packet in additional_packets]
packets.append
for signal in signals:
    packets.append(signal[0])
    packets.append(signal[1])

for i in range(len(packets)):
    min_packet = packets[i]
    for packet in packets[i+1:]:
        if compare_signal(min_packet, packet) == -1:
            min_packet = packet
    if min_packet != packets[i]:
        ind = packets.index(min_packet)
        packets[ind], packets[i] = packets[i], packets[ind]
total = 1
for packet in additional_packets:
    total *= packets.index(packet) + 1

print(total)
