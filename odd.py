def oddRange(L,R):
    oddnumber=[]
    for i in range(L,R+1):
        if i%2==1:
            oddnumber.append(i)

    return oddnumber

print(oddRange(3,4))

