#Write up to Hackerrank Missing Numbers
#Challenge : https://www.hackerrank.com/challenges/missing-numbers

from collections import Counter

n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

counterA = Counter(A)
counterB = Counter(B)

counterB.subtract(counterA)

missing = list(counterB.elements())
missing = list(set(missing))
missing.sort()
print(" ".join(list(map(str,missing))))


    