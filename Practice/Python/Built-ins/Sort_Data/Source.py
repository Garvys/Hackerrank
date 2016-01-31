from operator import *
N, M =[int(e) for e in input().split()]
l = list()
for i in range(N):
    l.append(list(map(int,input().split())))
K = int(input())
l.sort(key=itemgetter(K))
for e in l:
    print(" ".join(map(str,e)))