n = int(input())
a = set(map(int,input().split()))
m = int(input())
b = set(map(int,input().split()))
for elt in sorted(a ^ b):
    print(elt)