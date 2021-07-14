lis=[]
T=int(input())
for i in range(T):
    N=int(input())
    lis.append(N)

reverse=[]
for i in range(len(lis)):
    num=lis[i]
    reverse_num=0
    
    while num>0:
        reverse_num=reverse_num*10 + num%10
        num=num//10
    reverse.append(reverse_num)

for k in reverse:
    print(k)

