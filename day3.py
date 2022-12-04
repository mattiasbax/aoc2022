with open("day3_input.txt") as file:
    input_list = [line.rstrip() for line in file]


def convert_to_prio(char):
    return ord(
        char) - ord('A') + 27 if char.isupper() else ord(char) - ord('a') + 1


sum = 0
for input in input_list:
    half_len = int(len(input)/2)
    s0 = set(list(input)[:half_len])
    s1 = set(list(input)[half_len:])
    common_char = (s0 & s1).pop()
    prio = convert_to_prio(common_char)
    sum += prio

groups = [input_list[x:x+3] for x in range(0, len(input_list), 3)]
sum2 = 0
for group in groups:
    s0 = set(list(group[0]))
    s1 = set(list(group[1]))
    s2 = set(list(group[2]))
    common_char = (s0 & s1 & s2).pop()
    prio = convert_to_prio(common_char)
    sum2 += prio

print("Part 1 answer: ", sum)
print("Part 2 answer: ", sum2)
