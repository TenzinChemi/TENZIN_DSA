N=int(input())
A=[int(input()) for x in range(N)]
for j in range(1,N):
    key=A[j]
    i=j-1
    while i >= 0 and A[i]<key:
        A[i+1]=A[i]
        i-=1

    A[i+1]=key
     
print(A)

