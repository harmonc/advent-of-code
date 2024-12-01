pairs = open('day_01/input.txt', "r").read().split('\n')
listA = []
listB = []

for pair in pairs:
    a,b = pair.split('   ')
    listA.append(int(a))
    listB.append(int(b))

listA.sort()
listB.sort()

result = 0

for i, a in enumerate(listA):
    b = listB[i]
    result += abs(a-b)

print(result)