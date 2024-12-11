grid = list(open('day_08/input.txt', "r").read().split('\n'))
print(grid)

map = {}

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] != '.':
            if grid[row][col] in map:
                map[grid[row][col]].append([col,row])
            else:
                map[grid[row][col]] = [[col,row]]
            
print(map)

def getAntiNodes(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return [[a[0]+dx,a[1]+dy],[b[0]-dx,b[1]-dy]]

antinodes = []

h = len(grid)
w = len(grid[0])

print(w,h)

for key in map:
    for i in range(len(map[key])):
        for j in range(len(map[key])):
            if i != j:
                nodes = getAntiNodes(map[key][i],map[key][j])
                for node in nodes:
                    if (not node in antinodes) and (node[0] >= 0 and node[0] < w and node[1] >= 0 and node[1] < h):
                        antinodes.append(node)

print(antinodes)
print(len(antinodes))

answer = 0

print(answer)