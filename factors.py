def factors(number):
    count=0
    list=[]
    for i in range(1,number+1):
        if number % i == 0:
            count+=1
            list.append(i)
    return (count,list)

count,list=factors(6)

print(count)
print(list)
