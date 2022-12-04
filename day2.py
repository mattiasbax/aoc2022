
with open('day2_input.txt') as f:
    input_list_raw = [line.rstrip() for line in f]
    input_list = [tuple(line.split()) for line in input_list_raw]


score_map = {'A': 1, 'B': 2, 'C': 3}
score_map_2 = {'X': 0, 'Y': 3, 'Z': 6}
result_map = {'X': {'A': 3, 'B': 0, 'C': 6},
              'Y': {'A': 6, 'B': 3, 'C': 0},
              'Z': {'A': 0, 'B': 6, 'C': 3}}
result_map_2 = {'X': {'A': 'C', 'B': 'A', 'C': 'B'},
                'Y': {'A': 'A', 'B': 'B', 'C': 'C'},
                'Z': {'A': 'B', 'B': 'C', 'C': 'A'}}

score_1 = 0
for match in input_list:
    score_played = score_map[match[0]]
    score_match = result_map[match[1]][match[0]]
    score_1 += score_played + score_match

score_2 = 0
for match in input_list:
    score_played = score_map[result_map_2[match[1]][match[0]]]
    score_match = score_map_2[match[1]]
    score_2 += score_played + score_match

print("Part 1 answer:", score_1)
print("Part 2 answer:", score_2)
