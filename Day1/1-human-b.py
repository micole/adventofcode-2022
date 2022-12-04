'''
Prompt: write a program that adds groups of numbers together and prints out the largest group of numbers
'''

with open("1-input.txt", "r") as file:
    text = file.read()

groups = text.split("\n\n")

sorted_groups = []

for group in groups:
    current_group = sum(map(int, group.split('\n')))
    sorted_groups.append(current_group)

sorted_groups.sort(reverse=True)

print(sum(sorted_groups[:3]))