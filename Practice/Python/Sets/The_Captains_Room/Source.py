from collections import Counter

K = int(input())
roomsList = list(map(int,input().split()))
c = Counter(roomsList)
print(c.most_common()[::-1][0][0])