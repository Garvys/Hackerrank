n = int(input())
l = list(map(int,input().split()))
firstMax = max(l)
while max(l) == firstMax:
    l.remove(max(l))
print(max(l))