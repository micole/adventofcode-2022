'''
Instead of me trying to make a full solution with GPT I'm just going to document when I use it to generate something
'''

'''
Prompt: write a program where given two ranges of numbers it returns true if either range fully contains the other
'''
def range_fully_contains_other(range1, range2):
    start1, end1 = range1
    start2, end2 = range2
    return ((start1 <= start2 <= end1) and (start1 <= end2 <= end1)) or ((start2 <= start1 <= end2) and (start2 <= end1 <= end2))

'''
Prompt: write a function to split a string into two ranges of numbers. The format of the input will be a number followed by a dash followed by a number, separated by commas
'''
def split_string_into_ranges(s):
    range1, range2 = s.split(",")
    start1, end1 = map(int, range1.split("-"))
    start2, end2 = map(int, range2.split("-"))
    return ((start1, end1), (start2, end2))

'''
Prompt: write a program where given two ranges of numbers it returns true if one range contains the other
Issue, this doesn't work in both directions, so we need to actually pass it twice
'''
def range_contains_other(range1, range2):
    start1, end1 = range1
    start2, end2 = range2
    return (start1 <= start2 <= end1) or (start1 <= end2 <= end1)



number_of_pairs = 0

with open("4-input.txt", "r") as file:
    lines = file.readlines()

for index, line in enumerate(lines):
    #print(line)
    range1, range2 = split_string_into_ranges(line.strip())
    if range_contains_other(range1, range2) or range_contains_other(range2, range1):
        number_of_pairs += 1

print(number_of_pairs)

