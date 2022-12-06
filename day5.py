import re
import copy

with open("day5_input.txt") as f:
    input_list = [line.rstrip() for line in f]    
        
split_idx = input_list.index('')
cargo, actions  = [input_list[: split_idx], input_list[split_idx + 1: ]] 

cargo, indices = [cargo[:-1], cargo[-1]]
indices=list(map(int, list(indices.replace(' ',''))))

cargo_stacks= []
for idx in indices:
	cargo_stack = []
	for crate_row in cargo[::-1]:
		pos = 1+(idx-1)*4
		if pos <= len(crate_row):
			crate = crate_row[pos]
			if crate != ' ':
				cargo_stack.append(crate)		
	cargo_stacks.append(cargo_stack)

cargo_stacks_1 = copy.deepcopy(cargo_stacks)
cargo_stacks_2 = copy.deepcopy(cargo_stacks)
for action in actions:
	amount, from_stack, to_stack = tuple(map(int, re.findall('[0-9]+', action)))
	for i in range(amount):
		cargo_stacks_1[to_stack-1].append(cargo_stacks_1[from_stack-1].pop())
	for i in range(-amount,0):
		cargo_stacks_2[to_stack-1].append(cargo_stacks_2[from_stack-1].pop(i))
		
top_1 = [last for sub in cargo_stacks_1 for last in sub[-1]]
top_2 = [last for sub in cargo_stacks_2 for last in sub[-1]]

print("Answer to day 5 part 1: ", "".join(top_1))
print("Answer to day 5 part 2: ", "".join(top_2))