import numpy as np
from scipy.spatial.distance import cityblock

with open("day9_input.txt") as f:
    input_list = [(line.split()[0], int(line.split()[1]))
                  for line in f.readlines()]


def move_tail(tail, head):
    new_tail = tail
    delta = head - tail
    manhattan_distance = cityblock(list(head), list(tail))
    # print("#########################")
    #print("Head at: ", head)
    #print("Tail at: ", tail)
    #print("Delta: ", delta)
    #print("Distance", manhattan_distance)
    if (manhattan_distance == 2 and np.prod(delta) == 0) or manhattan_distance == 3:
        move = np.clip(delta, -1, 1)
        #print("moving: ", move)
        new_tail = tail + move
    elif manhattan_distance == 3:
        move = np.clip(delta, -1, 1)
        #print("moving: ", move)
        new_tail = tail + move
    #print("Moved tail to: ", new_tail)
    return new_tail


move_map = {'L': np.array([-1, 0]),
            'R': np.array([1, 0]),
            'U': np.array([0, 1]),
            'D': np.array([0, -1])}

#input_list = [('L', 5), ('U', 10)]

head = np.array([0, 0])
tail = [np.array([0, 0])]
visited = {tuple(tail)}

for direction, distance in input_list:
    for _ in range(distance):
        head = head + move_map[direction]
        tail = move_tail(tail, head)
        visited.add(tuple(tail))

print(len(visited))
