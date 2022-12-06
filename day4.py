with open("day4_input.txt") as f:
    input_list = [line.rstrip() for line in f]


def a_contains_b(a, b):
    return b[0] >= a[0] and b[1] <= a[1]


def a_overlaps_b(a, b):
    return b[0] <= a[0] <= b[1]


str_pairs = [str.split(',') for str in input_list]
contains = 0
overlaps = 0
for str_pair in str_pairs:
    a = tuple(map(int, str_pair[0].split('-')))
    b = tuple(map(int, str_pair[1].split('-')))

    if a_contains_b(a, b) or a_contains_b(b, a):
        contains += 1
    if a_overlaps_b(a, b) or a_overlaps_b(b, a):
        overlaps += 1

print("Part 1 answer: ", contains)
print("Part 2 answer: ", overlaps)
