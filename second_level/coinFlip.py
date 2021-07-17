for i in range(int(input())):
    G=int(input())
    for l in range(G):
        I,N,Q=map(int,input().split())
        sample=[]
    
        for i in range(N):
            sample.append(1)
        temp=sample
        tail=0
        head=0
        for j in range(len(sample)):
            for k in range(j):
                if(temp[k]==1):
                    temp[k]=0
                else:
                    temp[k]=1
        for k in temp:
            if k == 1:
                tail+=1
            else:
                head+=1
        if Q==2:
            print(tail)
        else:
            print(head)
    



