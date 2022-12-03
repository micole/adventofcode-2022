'''
Prompt: write a program that adds groups of numbers together and prints out the largest group of numbers
'''

import re

# Open the file and read its contents
with open("1-input.txt", "r") as file:
    text = file.read()

groups = text.split("\n\n")

# Find the longest group of consecutive numbers
largest_group = 0
current_group = 0
for group in groups:
    current_group = sum(map(int,group.split('\n')))
    if current_group > largest_group:
        largest_group = current_group
# Print the result
print(largest_group)
