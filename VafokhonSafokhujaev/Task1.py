
names = []

with open("../data/unsorted_names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

names = sorted(names)


with open("../data/sorted_names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")