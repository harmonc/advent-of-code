arr = list(map(int,open('2024/day_11/input.txt', "r").read().split(' ')))
            
print(arr)

set = {}

for num in arr:
    if num in set:
        set[num] += 1
    else:
        set[num] = 1

print(set)

def myAddToSet(set, key, value):
    result = set.copy()
    if key in result:
        result[key] += value
    else:
        result[key] = value
    return result
        

def cycle(set):
    result = {}
    for num in set:
        if num == 0:
            result = myAddToSet(result,1,set[num])
        elif len(str(num))%2==0:
            s = str(num)
            l = len(s)
            result = myAddToSet (result, int(s[0:int(l/2)]), set[num])
            result = myAddToSet (result, int(s[int(l/2):]), set[num])
        else:
            result = myAddToSet(result,num*2024,set[num])
    return result




for i in range(75):
    set = cycle(set)
    total = 0
    for k in set:
        total += set[k]
    print(i+1,total)


# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
