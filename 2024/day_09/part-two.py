line  = open('day_09/2024/input.txt', "r").read()

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

# printArr(arr)

def findFirstGap(arr, gapSize):
    currentGap = 0
    for i in range(len(arr)):
        if arr[i] == -1:
            currentGap += 1
            if currentGap == gapSize:
                return i - gapSize + 1
        else:
            currentGap = 0
    return -1

def countN(arr, n):
    result = 0
    for x in arr:
        if x == n:
            result += 1
    return result

def firstIndex(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1

def myFunc(arr):
    result = arr.copy()
    id = result[-1]
    while id >= 0:
        count = countN(result, id)
        index = firstIndex(result, id)
        gap_index = findFirstGap(result, count)
        print(id, index, count, gap_index)
        if gap_index >= 0 and gap_index < index:
            for i in range(count):
                result[gap_index+i] = id
                result[index+i] = -1
        id -= 1
        # printArr(result)
    return result



arr = myFunc(arr)
# printArr(arr)
answer = 0

for i in range(len(arr)):
    if arr[i]>0:
        answer += i * arr[i]

print(answer)