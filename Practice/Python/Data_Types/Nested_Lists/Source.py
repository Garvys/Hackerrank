from operator import itemgetter

n = int(input())
l = list()
for i in range(n):
    name = str(input())
    mark = float(input())
    l.append([name,mark])
firstMin = min(l,key=itemgetter(1))[1]
while min(l,key=itemgetter(1))[1] == firstMin:
    l.remove(min(l,key=itemgetter(1)))
secondMin = min(l,key=itemgetter(1))[1]
result = list()
while min(l,key=itemgetter(1))[1] == secondMin:
    result.append(min(l,key=itemgetter(1))[0])
    l.remove(min(l,key=itemgetter(1)))
    if len(l) == 0:
        break
result.sort()
for e in result:
    print(e)