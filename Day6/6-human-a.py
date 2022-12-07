def find_unique_4(line):
    a, b, c, d = line[0], line[1], line[2], line[3]
    for index, ch in enumerate(line):
        a = b
        b = c
        c = d
        d = ch
        if len(list(set([a,b,c,d]))) == 4:
            return index+1


with open("6-input.txt", "r") as file:
    lines = file.readlines()

for index, line in enumerate(lines):
    print(find_unique_4(line))