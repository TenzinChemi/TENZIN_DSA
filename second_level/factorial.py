def findTrailingZeros(n):
      
    # Initialize result
    count = 0
  
    # Keep dividing n by
    # powers of 5 and
    # update Count
    i = 5
    while (n / i>= 1):
        count += int(n / i)
        i *= 5
  
    return int(count)

T=int(input())
N=[]
for i in range(T):
    N.append(int(input()))

for j in N:
    print(findTrailingZeros(j))

