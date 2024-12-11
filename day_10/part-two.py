grid = list(map(list,open('day_10/input.txt', "r").read().split('\n')))

def myFunc(x,y,h):
    if x < 0 or y < 0 or x > len(grid[0])-1 or y > len(grid) - 1:
        return [[]]
    elif grid[y][x] == '9' and h == '9':
        return [[x,y]]
    elif grid[y][x] != h:
        return [[]]
    else:
        new_h = str(int(h)+1)
        result = []
        for arr in myFunc(x-1,y,new_h) + myFunc(x+1,y,new_h) + myFunc(x,y-1,new_h) + myFunc(x,y+1,new_h):
            if arr != []:
                result.append(arr)
        return result

answer = 0

for row in range(len(grid)):
    for col in range(len(grid)):
        if grid[row][col] == '0':
            result = myFunc(col,row,'0')
            print(result)
            answer += len(result)

print(answer)