
arr = open('2024/day_12/test_input.txt', "r").read().split('\n')

added = set()

regions = []

def getRegion(point):
    new_region = set()
    queue = []
    queue.append(point)
    flower = arr[point[1]][point[0]]
    while len(queue) > 0:
        curr = queue.pop(0)
        if arr[curr[1]][curr[0]] == flower:
            new_region.add(curr)
            added.add(curr)
            for v in [(0,1),(0,-1),(-1,0),(1,0)]:
                new_point = (curr[0]+v[0],curr[1]+v[1])
                if new_point[0] in range(len(arr[0])) and new_point[1] in range(len(arr[1])) and not new_point in added and not new_point in queue:
                    queue.append(new_point)
    return new_region, flower


def getCost(region):
    perimeter = 0
    for p in region:
        for v in [(1,0),(-1,0),(0,1),(0,-1)]:
            if not (p[0]+v[0],p[1]+v[1]) in region:
                perimeter += 1
    return perimeter * len(region)

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if not (j,i) in added:
            regions.append(getRegion((j,i)))

answer = 0
for region in regions:
    answer += getCost(region[0])

print(answer)