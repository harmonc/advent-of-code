grid = open('day_06/test_input.txt', "r").read().split('\n')
gridTrack = grid.copy()
dir = 0
x = 0
y = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '^':
            y = i
            x = j

# print('\n'.join(grid))


def replaceN(str, n, c):
    if n == len(str):
        return str[0:n]+c
    return str[0:n] + c + str[n+1:]

def move(x,y,dx, dy, sym):
    if grid[y+dy][x+dx] == '.':
        grid[y+dy] = replaceN(grid[y+dy],x+dx,sym)
        grid[y] = replaceN(grid[y],x,'.')
        return x + dx, y + dy
    return x, y
end = False
while not end:
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
    except:
        end = True

    gridTrack[y] = replaceN(gridTrack[y],x,'X')

    if x == nx and y == ny:
        dir = (dir + 1)%4
    
    x = nx
    y = ny
    # print()
    # print('\n'.join(grid))

answer = 0

print('\n'.join(gridTrack))

for line in gridTrack:
    for i in range(len(line)):
        if line[i]=='X':
            answer+=1

print(answer)