str = open('day_04/input.txt', "r").read()
grid = list(map(list,str.split('\n')))

xmas = ['X','M','A','S']

result = 0

for row in range(len(grid)):
    for i in range(len(grid[row])-3):
        if grid[row][i:i+4]==xmas or list(reversed(grid[row][i:i+4]))==xmas:
            result += 1

for row in range(len(grid)-3):
    for col in range(len(grid[0])-3):
        str = [grid[row][col],grid[row+1][col+1],grid[row+2][col+2],grid[row+3][col+3]]
        if str == xmas or list(reversed(str)) == xmas:
            result += 1

for row in range(3,len(grid)):
    for col in range(0,len(grid[0])-3):
        str = [grid[row][col],grid[row-1][col+1],grid[row-2][col+2],grid[row-3][col+3]]
        if str == xmas or list(reversed(str)) == xmas:
            result += 1

grid = [[row[i] for row in grid] for i in range(len(grid[0]))]

for row in range(len(grid)):
    for i in range(len(grid[row])-3):
        if grid[row][i:i+4]==xmas or list(reversed(grid[row][i:i+4]))==xmas:
            result += 1

print(result)