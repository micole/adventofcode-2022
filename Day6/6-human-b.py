def find_unique(line, num):
    line = ("-" * num) + line
    for index, ch in enumerate(line):
        if len(list(set(line[index:index+num]))) == num:
            return index


with open("6-input.txt", "r") as file:
    lines = file.readlines()

for index, line in enumerate(lines):
    print(find_unique(line,14))