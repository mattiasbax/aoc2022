with open('day7_input.txt') as f:
    input_lines = [line.rstrip() for line in f]

path = ""
files = dict()
directories = dict()
for line in input_lines:
    if line[0:4] == "$ cd" and line[5:7] != "..":
        path += line[5:]+"/"
        directories[path] = 0
    if line[5:7] == "..":
        lastdir = path.rfind("/")
        lastdir2 = path[:lastdir].rfind("/")
        path = path[:lastdir2+1]
    if line.split(" ")[0].isnumeric() == True:
        file = path+line.split(" ")[1]
        files[file] = line.split(" ")[0]
        directories[path] += int(line.split(" ")[0])

totalsize = 0  # calculating part 2
for key in files:
    totalsize += int(files[key])
smallest = 70000000
freespace = 70000000-totalsize
total = 0
for key in directories:
    currentpath = key
    while len(currentpath) > 2:
        parent = currentpath[:currentpath[:currentpath.rfind(
            "/")].rfind("/")+1]
        directories[parent] += directories[key]
        currentpath = parent

for key in directories:  # calculating part 1
    if directories[key] < 100000:
        total += directories[key]

    if freespace+directories[key] > 30000000:  # calculating part 2
        if smallest > directories[key]:
            smallest = directories[key]

print("Answer to day 7 part 1: ", total)
print("Answer to day 7 part 2: ", smallest)
