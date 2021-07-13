N=int(input())
number=1
l=1
while l<=N:
    for i in range(number,number+5):
        print(i,end=" ")
    print()

    for j in range(i+5,i,-1):
        print(j,end=" ")
    number=j+5

    print()
    l+=2
