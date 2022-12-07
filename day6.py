
from collections import Counter

with open('day6_input.txt') as f:
    input_list = [line.rstrip() for line in f]


def find_marker(signal, marker_length):
    for i in range(len(signal)-marker_length):
        sub = Counter(signal[i:i+marker_length])
        if len(sub) == marker_length:
            return i+marker_length


print("Answer to day 5 part 1: ", find_marker(input_list[0], 4))
print("Answer to day 5 part 2: ", find_marker(input_list[0], 14))
