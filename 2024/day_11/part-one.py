arr = list(map(int,open('2024/day_11/input.txt', "r").read().split(' ')))
            
print(arr)

def cycle(arr):
    result = []
    for num in arr:
        if num == 0:
            result.append(1)
        elif len(str(num))%2==0:
            s = str(num)
            l = len(s)
            result.append(int(s[0:int(l/2)]))
            result.append(int(s[int(l/2):]))
        else:
            result.append(num*2024)
    return result


for i in range(25):
    arr = cycle(arr)


print(len(arr))

# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
