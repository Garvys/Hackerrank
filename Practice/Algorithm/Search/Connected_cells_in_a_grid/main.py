n = int(input())
m = int(input())
rows = []
visited = []

for _ in range(n):
    rows.append(list(map(int,input().split())))
    visited.append([False for _ in range(m)])
    
sizeMax = 0
regions = []
def rec(line,col,sizeRegion):
    global sizeMax
    if line >= 0 and line < n and col >= 0 and col < m and not visited[line][col] and rows[line][col] == 1:
        visited[line][col] = True
        sizeRegion += 1
        if sizeRegion > sizeMax:
            sizeMax = sizeRegion
        sizeRegion = rec(line-1,col-1,sizeRegion)
        sizeRegion = rec(line-1,col,sizeRegion)
        sizeRegion = rec(line-1,col+1,sizeRegion)
        sizeRegion = rec(line,col-1,sizeRegion)
        sizeRegion = rec(line,col+1,sizeRegion)
        sizeRegion = rec(line+1,col-1,sizeRegion)
        sizeRegion = rec(line+1,col,sizeRegion)
        sizeRegion = rec(line+1,col+1,sizeRegion)
    return sizeRegion

for i in range(n):
    for j in range(m):
           rec(i,j,0)
                        


print(sizeMax)