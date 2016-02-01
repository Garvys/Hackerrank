l = list(str(input()))
index, c = input().split()
l[int(index)] = str(c)
print("".join(l))