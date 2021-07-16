N=int(input())
maxSpeed=[]
while(N>0):
    numberCar=int(input())
    speedCar=[]
    count=1
    speedCar=[int(i) for i in input().split()][:numberCar]
    
    if numberCar<=1:
        maxSpeed.append(count)
    else:    
        for i in range(0,len(speedCar)-1):
            
            if speedCar[i] > speedCar[i+1]:
                count+=1
        maxSpeed.append(count)     
    N-=1
for i in maxSpeed:
    print(i)

