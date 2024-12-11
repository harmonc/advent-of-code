line  = open('day_09/test_input.txt', "r").read()
print(line)

arr = []
for i in range(len(line)):
    if i % 2 == 0:
        for j in range(int(line[i])):
            arr.append(int(i/2))
    elif i % 2 == 1:
        for j in range(int(line[i])):
            arr.append(-1)

def printArr(a):
    result = ''
    for n in a:
        if n == -1:
            result += '.'
        else:
            result += str(n)
    print(result)

printArr(arr)

def myFunc(arr):
    result = arr.copy()
    empty = 0
    last = len(result)-1
    while empty < last-1:
        if result[empty]==-1:
            while result[last]==-1:
                last -= 1
            print(last, empty, arr[last])
            result[empty] = result[last]
            result[last] = -1
        empty += 1

    return result



arr = myFunc(arr)

answer = 0

for i in range(len(arr)):
    if arr[i]>0:
        answer += i * arr[i]

print(answer)