T=int(input())

for t in range(T):
    k,d0,d1=[int(x) for x in input().split()]
    digit=0
    sum_two=d0+d1
    val=d0*10
    value=val+d1
    for i in range(2,k):
        rem = sum_two % 10
        val=value*10
        value=val+rem
        sum_two=sum_two+rem
    if value % 3 == 0:
        print('YES')
    else:
        print('NO')




