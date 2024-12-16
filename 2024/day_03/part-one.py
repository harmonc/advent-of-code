import re

line = open('2024/day_03/test_input.txt', "r").read()

arr = re.findall("mul\((\d+),(\d+)\)", line)

result = 0

for pair in arr:
    result += int(pair[0])*int(pair[1])

print(result)