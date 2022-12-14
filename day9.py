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
    print("Head at: ", head)
    print("Tail at: ", tail)
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
    print("Moved tail to: ", new_tail)
    return new_tail


move_map = {'L': np.array([-1, 0]),
            'R': np.array([1, 0]),
            'U': np.array([0, 1]),
            'D': np.array([0, -1])}

input_list = [('L', 5), ('U', 10)]
number_of_knots=10
knots = [np.array([0, 0])]*number_of_knots
visited_1 = {tuple(knots[1])}
visited_10 = {tuple(knots[-1])}

for direction, distance in input_list:
    for _ in range(distance):
        for idx, knot in enumerate(knots):	
        	if idx == 0:
        		knot[idx] = knot[idx] + move_map[direction]
        		print(knot[idx])
        	else:
        		knot = move_tail(knot, knots[idx-1])
        visited_1.add(tuple(knots[1]))
        visited_10.add(tuple(knots[9]))

print(len(visited_1))
print(len(visited_10))
