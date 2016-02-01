n = int(input())
s = set(map(int, input().split())) 
N = int(input())
for i in range(N):
    cmd = list(map(str,input().split()))
    if cmd[0] == "pop":
        s.pop()
    elif cmd[0] == "remove":
        s.remove(int(cmd[1]))
    elif cmd[0] == "discard":
        s.discard(int(cmd[1]))
    else:
        print("Commande non gérée")
print(sum(s))