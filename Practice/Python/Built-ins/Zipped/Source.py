N,X = [int(e) for e in input().split()]
listByStudents = list()
for i in range(X):
    listByStudents.append(list(map(float,input().split())))
listByDicipline = list(zip(*listByStudents))
for marks in listByDicipline:
    res = 0.0;
    for m in marks:
        res += m
    print(res/X)