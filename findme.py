N , K = map(int, input().split())
A=[int(i) for i in input().split()][:N]
flag=False
for i in range(N):
    if A[i]==K:
        flag=True

if flag:
    print("1")

else:
    print("-1")