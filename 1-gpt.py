'''
Prompt: write a program that adds groups of numbers together and prints out the largest group of numbers
'''

import re

# Open the file and read its contents
with open("numbers.txt", "r") as file:
    text = file.read()

# Use a regular expression to extract all numbers from the file
numbers = re.findall(r"\d+", text)

# Convert the numbers to integers
numbers = [int(number) for number in numbers]

# Sort the numbers in ascending order
numbers.sort()

# Find the longest group of consecutive numbers
longest_group = []
current_group = []
for number in numbers:
    if not current_group:
        # Start a new group
        current_group.append(number)
    elif number == current_group[-1] + 1:
        # Add the number to the current group
        current_group.append(number)
    else:
        # The current group has ended, so save it if it's the longest so far
        if len(current_group) > len(longest_group):
            longest_group = current_group
        # Start a new group
        current_group = [number]

# Check if the last group is the longest
if len(current_group) > len(longest_group):
    longest_group = current_group

# Add the numbers in the longest group together
result = sum(longest_group)

# Print the result
print(result)