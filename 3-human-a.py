# Because I'll be creating a few functions, I'll just create gpt in line for this problem

'''
prompt: write a function that splits a string evenly

This code defines a function split_string() that takes two arguments: a string s and an integer n. The function returns a list of strings, each representing a split of s.
'''
from typing import List


def split_string(s: str, n: int) -> List[str]:
    # calculate length of each split
    length = len(s) // n

    # split the string into n equal parts
    return [s[i*length:(i+1)*length] for i in range(n)]

'''
Prompt: write a function that takes two strings and returns letters that exist in both
'''
def common_letters(s1: str, s2: str) -> str:
    # create a set of characters from s1
    s1_set = set(s1)

    # create a set of characters from s2
    s2_set = set(s2)

    # find the intersection of the two sets
    common = s1_set.intersection(s2_set)

    # convert the set to a string and return it
    return ''.join(common)

'''
I actually had a lot of issues trying to get this function to exist.
Most prompts like: write a function that converts letters to their position in the alphabet with lowercase a starting at 1 and uppercase A starting at 27
immediately lowercased the input. Instead I had to write a prompt like this:
Prompt: write a function that takes a characters ord location subtracted by ord('a')+1

Note: because capitals show up first I edited this a bit and put more logic when calling this function
Essentially this function wasn't written by GPT, but it did remind me `ord` existed.
'''
def convert_to_number(ch: str) -> int:
    # convert the character to a number
    if ch.isupper():
        return ord(ch) - ord('A') + 27
    return ord(ch) - ord('a') + 1


total_rucksack = 0

# Now with those out the way, lets write it out
with open("3-input.txt", "r") as file:
    lines = file.readlines()

for index, line in enumerate(lines):
    a, b = split_string(line, 2)
    letters = common_letters(a, b)
    for letter in letters:
        total_rucksack += convert_to_number(letter)

print(total_rucksack)