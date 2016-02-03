input()
A = set(map(int,input().split()))
N = int(input())
for i in range(N):
    cmd = list(map(str,input().split()))
    B = set(map(int,input().split()))
    if cmd[0] == "intersection_update":
        A &= B
    elif cmd[0] == "update":
        A |= B
    elif cmd[0] == "symmetric_difference_update":
        A ^= B
    elif cmd[0] == "difference_update":
        A -= B
    else:
        print("Commande non gérée")
print(sum(A))