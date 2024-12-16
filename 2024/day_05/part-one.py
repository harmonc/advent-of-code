rules,updates = open('2024/day_05/input.txt', "r").read().split('\n\n')

def myMap(str):
    return list(map(int,str.split('|')))

rules = list(map(myMap,rules.split('\n')))

def checkRule(id, arr, rule):
    result = True
    if arr[id] == rule[0]:
        for i in range(id):
            if arr[i] == rule[1]:
                result = False
    elif arr[id] == rule[1]:
        for i in range(id,len(arr)):
            if arr[i] == rule[0]:
                result = False
    return result

answer = 0


for update in updates.split('\n'):
    arr = list(map(int,update.split(',')))
    result = True
    for i in range(len(arr)):
        for rule in rules:
            if not checkRule(i,arr,rule):
                result = False
    if result:
        answer += arr[int(len(arr)/2)]


print(answer)