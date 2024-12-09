grid_original = open('day_06/input.txt', "r").read().split('\n')
grid = grid_original.copy()



part_one_answer= open('day_06/answer1.txt', "r").read().split('\n')

print(part_one_answer)

spots = []

for row in range(len(part_one_answer)):
    for col in range(len(part_one_answer[row])):
        if part_one_answer[row][col] == 'X':
            spots.append([col,row])

# print('\n'.join(grid))
class OutOfBounds(Exception):
    pass

def replaceN(str, n, c):
    result = str[0:n] + c + str[n+1:]
    return result[0:len(str)]

def move(x,y,dx, dy, sym):

    if x + dx < 0 or y + dy < 0:
        raise OutOfBounds("Out of Bounds")

    if grid[y+dy][x+dx] == '.':
        grid[y+dy] = replaceN(grid[y+dy],x+dx,sym)
        grid[y] = replaceN(grid[y],x,'.')
        return x + dx, y + dy
    return x, y

answer = 0

def printTrack():
    str = ''
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            h = gridTrack[i][j]
            # print(h)
            if grid[i][j] == '#':
                str += '#'
            elif grid[i][j]=='O':
                str+='O'
            elif 0 in h or 2 in h and not (1 in h or 3 in h):
                str += '|'
            elif not (0 in h or 2 in h) and (1 in h or 3 in h):
                str += '-'
            elif len(h)>0:
                str += '+'
            else:
                str += '.'
        str += '\n'
    print(str)

# TODO:
# Loop through the Xs in the track from part one
#
#
#

# 2625
print(len(spots))
for i in range(len(spots)):
    print(answer, i/len(spots)*100)
    j,i = spots[i]
    if grid_original[i][j] == '.':
        dir = 0
        x = 0
        y = 0
        for i3 in range(len(grid_original)):
            for j3 in range(len(grid_original[i3])):
                if grid_original[i3][j3] == '^':
                    y = i3
                    x = j3
        startX = x
        startY = y
        gridTrack = {}
        # print(gridTrack)
        grid = grid_original.copy()
        grid[i] = replaceN(grid[i],j,'O')
        # print('\n'.join(grid.copy()))
        end = False
        loop = False
        while not end:
            px = x
            py = y
            nx = x
            ny = y
            try:
                if dir == 0:
                    nx,ny = move(x,y,0,-1,'^')
                elif dir == 1:
                    nx,ny = move(x,y,1,0,'>')
                elif dir == 2:
                    nx,ny = move(x,y,0,1,'v')
                elif dir == 3:
                    nx,ny = move(x,y,-1,0,'<')
            except Exception as error:
                print(error)
                end = True

            # gridTrack[y] = replaceN(gridTrack[y],x,'X')
            # print('\n'.join(gridTrack))

            # print(dir)
            
            if str(px)+","+str(py) in gridTrack:
                gridTrack[str(px)+","+str(py)].append(dir)
            else:
                gridTrack[str(px)+","+str(py)] = [dir]
            # print(gridTrack)
            if x == nx and y == ny:
                dir = (dir + 1)%4
            else:
                if str(nx)+','+str(ny) in gridTrack:
                    if dir in gridTrack[str(nx)+','+str(ny)]:
                        # print(gridTrack)
                        # print(nx,ny,dir)
                        end = True
                        loop = True
        
            x = nx
            y = ny
    

            # # print(gridTrack)
            # if loop:
                # print('loop', loop)
                # print(gridTrack)
                # printTrack()
            if loop:
                # print(gridTrack)
                answer += 1

# print()
# print('\n'.join(grid))




print(answer)