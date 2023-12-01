import re

# Input 
with open("input.txt") as f:
    puzzle_input = [line.strip() for line in f.readlines()]


def find_digits(line):
    pattern = r"\d"
    return [int(digit) for digit in re.findall(pattern, line)]

def find_first_last_digit(line):
    digit_words = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    pattern = r"one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9"
    first = re.search(pattern, line).group()
    reverse_line = line[::-1]
    index = 0
    while index <= len(reverse_line):
        search_line = reverse_line[:index][::-1]
        match = re.search(pattern, search_line)
        if match:
            last = match.group()
            break
        index += 1
    if first in digit_words.keys():
        first = digit_words[first]
    if last in digit_words.keys():
        last = digit_words[last]
    return [first, last]

def combine_digits(line):
    combined = "{0}{1}".format(line[0], line[-1])
    return int(combined)

def day1_part1(puzzle_input):
    digit_lines = []
    for line in puzzle_input:
        digit_lines.append(find_digits(line))
    solution = sum(map(combine_digits, digit_lines))
    print("Part 1 Solution: {0}".format(solution))
    return solution

def day1_part2(puzzle_input):
    digit_lines = list(map(find_first_last_digit, puzzle_input))
    solution = sum(map(combine_digits, digit_lines))
    print("Part 2 Solution: {0}".format(solution))
    return solution

# Soluzione_p1
day1_part1(puzzle_input)

# Soluzione_p2
day1_part2(puzzle_input)
