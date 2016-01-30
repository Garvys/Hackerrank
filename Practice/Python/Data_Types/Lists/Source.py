N = int(input())

myList = list()

for i in range(N):
    cmd = input().split()
    if cmd[0] == "append":
        myList.append(int(cmd[1]))
    elif cmd[0] == "insert":
        myList.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0] == "remove":
        myList.remove(int(cmd[1]))
    elif cmd[0] == "pop":
        myList.pop()
    elif cmd[0] == "index":
        myList.index(int(cmd[1]))
    elif cmd[0] == "count":
        myList.count(int(cmd[1]))
    elif cmd[0] == "sort":
        myList.sort()
    elif cmd[0] == "reverse":
        myList.reverse()
    elif cmd[0] == "print":
        print(myList)
    else:
        print("Commande non reconnue")