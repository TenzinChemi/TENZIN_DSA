N=int(input())
while(N>0):
    numberCar=int(input())
    speedCar=[]
    count=1
    l=[int(i) for i in input().split()][:numberCar]
    
    fast=l[0]
    for i in range(1,numberCar):
        if l[i]<=fast:
            count+=1
            fast=l[i]
    N-=1
    print(count)

