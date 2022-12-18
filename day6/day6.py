file = open('transmission.txt', 'r')

transmission = file.readline()


def find_pattern(pat: int) -> int:
    for i in range(pat, len(transmission)):
        for j in range(1, pat):
            if transmission[i-j] in transmission[i-pat:i-j]:
                break
        else:
            return i

packet = 4

packet_char = find_pattern(packet)

print(f'How many characters for packet: {packet_char}')

message = 14

message_char = find_pattern(message)

print(f'How many characters for message: {message_char}')
