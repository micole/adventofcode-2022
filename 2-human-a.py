# Thanks GPT, I'll just write some wrapper work around your function

def calculate_score(opponent: str, choice: str) -> int:
    score = 0

    # check for win/loss
    if opponent == choice:
        score = 3
    elif opponent == 'A' and choice == 'B':
        score = 6
    elif opponent == 'B' and choice == 'C':
        score = 6
    elif opponent == 'C' and choice == 'A':
        score = 6

    # add bonus points for choice
    if choice == 'A':
        score += 1
    elif choice == 'B':
        score += 2
    elif choice == 'C':
        score += 3

    return score

overall_score = 0

convert = {'X': 'A', 'Y': 'B', 'Z': 'C'}

with open("2-input.txt", "r") as file:
    lines = file.readlines()

for index, line in enumerate(lines):
    #print(line)
    opponent, choice = line.split(" ")
    overall_score += calculate_score(opponent, convert[choice.strip()])

print(overall_score)

