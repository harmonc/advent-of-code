import re

line = open('day_03/test_input_2.txt', "r").read()

arr = re.findall("mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line)

result = 0
do = True

for instruct in arr:
    if instruct[0] == '':
        if instruct[3] == "don't()":
            do = False
        if instruct[2] == 'do()':
            do = True
    elif do:
        result += int(instruct[0])*int(instruct[1])

print(result)