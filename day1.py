from itertools import groupby

with open("day1_input.txt") as file:
    input_list = [line.rstrip() for line in file]

split_list = [list(sub) for ele, sub in groupby(input_list, key=bool) if ele]
int_list = [[int(i) for i in sub] for sub in split_list]
sum_list = [sum(sub) for sub in int_list]
sum_list.sort()
max = sum_list[-1]
max3 = sum(sum_list[-3:])

print("Part 1 answer: ", max)
print("Part 2 answer: ", max3)
