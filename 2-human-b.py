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

'''
New GPT function (with a small edit)
Prompt: write a function where you calculate what you need to choose in a game of rock paper scissors based on the input of what your opponent is going to play and the result of win, lose, or draw 
No modifications, but 'return X' is never going to happen so could be removed
'''

def calculate_choice(opponent: str, result: str) -> str:
    if result == 'win':
        if opponent == 'A':
            return 'B'  # play paper to win against rock
        elif opponent == 'B':
            return 'C'  # play scissors to win against paper
        elif opponent == 'C':
            return 'A'  # play rock to win against scissors
        else:
            return 'X'  # play rock by default
    elif result == 'lose':
        if opponent == 'A':
            return 'C'  # play scissors to lose against rock
        elif opponent == 'B':
            return 'A'  # play rock to lose against paper
        elif opponent == 'C':
            return 'B'  # play paper to lose against scissors
        else:
            return 'X'  # play rock by default
    elif result == 'draw':
        if opponent == 'A':
            return 'A'  # play rock to draw against rock
        elif opponent == 'B':
            return 'B'  # play paper to draw against paper
        elif opponent == 'C':
            return 'C'  # play scissors to draw against scissors
        else:
            return 'X'  # play rock by default
    else:
        return 'X'  # play rock by default


overall_score = 0

convert = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}

with open("2-input.txt", "r") as file:
    lines = file.readlines()

for index, line in enumerate(lines):
    #print(line)
    opponent, strategy = line.strip().split(" ")
    thrown = calculate_choice(opponent, convert[strategy])
    overall_score += calculate_score(opponent, thrown)

print(overall_score)

