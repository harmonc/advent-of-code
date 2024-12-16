pairs = open('2024/day_01/input.txt', "r").read().split('\n')
listA = []
mapB = {}

for pair in pairs:
    a,b = pair.split('   ')
    listA.append(int(a))
    if int(b) in mapB:
        mapB[int(b)] = mapB[int(b)]+1
    else:
        mapB[int(b)] = 1

listA.sort()
result = 0

for a in listA:
    if a in mapB:
        result += a * mapB[a]

print(result)