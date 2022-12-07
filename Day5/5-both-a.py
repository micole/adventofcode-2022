'''
This challenge was harder to try to implement.
After a while of dealing with trying to send in the input datastructure I instead opted to teach it what I cared about
'''

'''
Prompt: write a function that puts every 4th character of a line (starting at the 2nd character) and returns them as a list

Funny note, this didn't return the result. So I've added that line
'''

def extract_every_fourth(line):
    # Initialize an empty list
    result = []

    # Iterate over the characters in the line, starting at the 2nd character
    for i in range(1, len(line), 4):
        # Add the character to the list
        result.append(line[i])

    return result # Human line


'''
Prompt: write a function that takes a list of lists and converts it to a vertical stack
'''

def to_vertical_stack(lists):
    # Calculate the maximum number of items in the inner lists
    max_items = max([len(lst) for lst in lists])

    # Create a new list with the same number of inner lists as the original list,
    # each inner list having the same number of items as the maximum number of items
    # found in the original list of lists
    stacked = [[] for _ in range(max_items)]

    # Iterate over the original list of lists
    for lst in lists:
        # Iterate over the items in the current list
        for i, item in enumerate(lst):
            # Append the current item to the corresponding inner list in the stacked list
            stacked[i].append(item)

    return stacked

'''
Prompt: write a function that given a list of lists removes an item if it is a single space character

bug fix: pop from enumerated list means you skip spaces, so I'm editing to make a new list
'''
def remove_single_spaces(lists):
    overall_lists = []
    # Iterate over the original list of lists
    for lst in lists:
        new_list = []
        # Buggy code
        # Iterate over the items in the current list
        for i, item in enumerate(lst):
            if item != " ":
                new_list.append(item)
            # If the current item is a single space character, remove it from the list
            #if item == " ":
                #lst.pop(i)
        overall_lists.append(new_list)

    return overall_lists

'''
ChatGPT isn't responding currently, so I'll make a pop function
'''
def move_items(listfrom, listto):
    listto.insert(0, listfrom.pop(0))
    return(listfrom, listto)


with open("5-input.txt", "r") as file:
    lines = file.readlines()

lists = []
for index, line in enumerate(lines):
    if line == '\n':
        break
    lists.append(extract_every_fourth(line))

vertical_list = to_vertical_stack(lists[:-1])
clean_list = remove_single_spaces(vertical_list)
print(clean_list)

for index, line in enumerate(lines):
    if line.startswith("move"):
        commands = line.strip().split(" ")
        print(line)
        for i in range(int(commands[1])):
            clean_list[int(commands[3])-1], clean_list[int(commands[5])-1] = move_items(clean_list[int(commands[3])-1], clean_list[int(commands[5])-1])
    print(clean_list)

for list in clean_list:
    print(list[0])