N=int(input())
even=0
odd=0
for i in range(N+N+1):
    if i % 2 == 0:
        even+=i
    else:
        odd+=i

print(f"{odd} {even}")
