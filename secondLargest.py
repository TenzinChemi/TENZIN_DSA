def secondLargest(a,b,c):
    if (a>b and a<c) or (a<b and a>c):
        return a
    
    elif (b<a and b>c) or (b>a and b<c):
        return b

    else:
        return c

print(secondLargest(2,7,21))
