def divisible(N):
    if N%5 == 0 and N % 11 == 0:
        return "BOTH"

    elif N%5 == 0 or N%11 == 0:
        return "ONE"

    else:
        return "NONE"

print(divisible(110))
def testdiv():
    for i in range (1,1000):
        print(f"{i} is divisible of {divisible(i)} 5 and 11")


