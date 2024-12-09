def myMap(line):
    return line.split(': ')


lines = list(map(myMap,open('day_07/input.txt', "r").read().split('\n')))

def myFunc(factors, kernal, ans):
    if len(factors) == 0:
        return kernal == ans
    else:
        return myFunc(factors[1:], kernal + factors[0],ans) or myFunc(factors[1:], kernal * factors[0], ans)

answer = 0

for ans, factors in lines:
    factors = list(map(int,factors.split(' ')))
    if myFunc(factors[1:],factors[0],int(ans)):
        answer += int(ans)






print(answer)