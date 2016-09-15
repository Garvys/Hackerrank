#Write up for Hacckerrank Kangoroo
#Challenge : https://www.hackerrank.com/challenges/kangaroo

import sys
x1, v1, x2, v2 = list(map(int,input().split()))

if v1 != v2:
    k = float(x1 - x2) / (v2 - v1)
    res = int(k) == k and k >= 0
else:
    res = x1 == x2

if res:
	print('YES')
else:
	print('NO')