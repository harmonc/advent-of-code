rules,updates = open('day_05/input.txt', "r").read().split('\n\n')

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



def inCorrectOrder(arr):
    result = True
    for i in range(len(arr)):
        for rule in rules:
            if not checkRule(i,arr,rule):
                result = False
    return result

def mapUpdate(update):
    return list(map(int,update.split(',')))


updates = list(filter(lambda x : not inCorrectOrder(x),list(map(mapUpdate,updates.split('\n')))))




def correctOrder(arr):
    result = arr.copy()
    change = True
    while change:
        countChange = 0
        for rule in rules:
            if rule[0] in result and rule[1] in result:
                ai = result.index(rule[0])
                bi = result.index(rule[1])
                if ai > bi:
                    countChange+=1
                    temp = result[ai]
                    result[ai] = result[bi]
                    result[bi] = temp
        if countChange == 0:
            change = False
    return result
    


answer = 0

for update in updates:
    corrected = correctOrder(update)
    answer += corrected[int(len(corrected)/2)]
   


print(answer)