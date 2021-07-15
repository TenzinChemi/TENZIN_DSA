T=int(input())
lis=[]
for i in range(T):
    N=int(input())
    lis.append(N)
profites=[]
asc=sorted(lis)
for x in range(len(asc)):
    profites.append(asc[x]*T)
    T-=1
print(max(profites))
