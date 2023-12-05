import re


def score_line(line):
    m = re.match(r"Card\s+(\d+):\s+(.*?)\s\|\s+(.*?)$", line)
    wins = set(int(n) for n in m.group(2).strip().split())
    nums = set(int(n) for n in m.group(3).strip().split())
    return wins.intersection(nums)


p1 = 0

lines = open("input.txt").read().strip().splitlines()

p2 = [1] * len(lines)

for n, line in enumerate(lines):
    matches = score_line(line)
    p1 += int(2 ** (len(matches) - 1))
    for i in range(len(matches)):
        p2[n + i + 1] += p2[n]

print(f"Parte 1: {p1}")
print(f"Parte 2: {sum(p2)}")
