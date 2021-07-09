N=int(input())
A=[int(i) for i in input().split()][:N]

for i in range(N-1,-1,-1):
    print(A[i],end=" ")