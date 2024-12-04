str = open('day_04/input.txt', "r").read()
grid = list(map(list,str.split('\n')))

mas = ['M','A','S']

result = 0

for row in range(len(grid)-2):
    for col in range(len(grid[row])-2):
        d1 = [grid[row][col],grid[row+1][col+1],grid[row+2][col+2]]
        d2 = [grid[row+2][col],grid[row+1][col+1],grid[row][col+2]]
        if (d1 == mas or list(reversed(d1)) == mas) and (d2 == mas or list(reversed(d2)) == mas):
            result += 1


print(result)