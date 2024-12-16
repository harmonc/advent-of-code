import re

arr = open('day_13/input.txt', "r").read().split('\n\n')
            
def myFunc(str):
    result_arr = str.split('\n')
    a = re.findall("X\+(\d+), Y\+(\d+)", result_arr[0])[0]
    b = re.findall("X\+(\d+), Y\+(\d+)", result_arr[1])[0]
    c = re.findall("X\=(\d+), Y\=(\d+)", result_arr[2])[0]
    result = 9999
    for i in range(100):
        for j in range(100):
            if int(a[0]) * i + int(b[0]) * j == int(c[0]) and int(a[1]) * i + int(b[1]) * j == int(c[1]) and i * 3 + j < result:
                result = i * 3 + j
    if result == 9999:
        return 0
    return result

answer = 0
for str in arr:
    answer += myFunc(str)

print(answer)