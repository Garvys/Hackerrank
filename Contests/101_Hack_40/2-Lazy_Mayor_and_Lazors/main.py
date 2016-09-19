n = int(input())
h = list(map(int,input().split()))
m = int(input())
x_l = list(map(int,input().split()))
x_l.sort()

imin = 0
for x in x_l:
    nothingRemoved = True
    for i in range(imin,x-1):
        if h[i] > (x - (i+1)):
            if nothingRemoved:
                imin = i + 1
            nothingRemoved = False
            h[i] =  x-(i+1)
print(sum(h))
    