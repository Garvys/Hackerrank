from collections import Counter
X = int(input())
sizeShoesAvailable = Counter(list(map(int,input().split())))
N = int(input())
res = 0
for i in range(N):
    size, price = list(map(int,input().split()))
    if sizeShoesAvailable[size] > 0:
        res += price
        sizeShoesAvailable.subtract({size : 1})
print(res)
    