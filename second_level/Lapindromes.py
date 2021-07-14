lis=[]
T=int(input())
for i in range(T):
    N=input()
    lis.append(N)
    
for j in range(len(lis)):
    length=len(lis[j])//2
    word=lis[j]
    if len(lis[j])%2==1:
        left=word[:length]
        right=word[length+1:]
    else:
        left=word[:length]
        right=word[length:]
        
    flag=False
    freq=right
    count=0
    for k in left:
        for l in freq:
            if k==l:
                freq=right.replace(l,"",1)
                count+=1
                if count==len(left):
                    flag=True
                break
    if flag:
        print("YES")

    else:
        print("NO")


