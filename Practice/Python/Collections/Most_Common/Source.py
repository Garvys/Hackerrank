import collections
s = str(input())
count = collections.Counter(s)
for i in sorted(count.items(), key=lambda x:(-x[1], x[0]))[:3]:
    print(i[0], i[1])