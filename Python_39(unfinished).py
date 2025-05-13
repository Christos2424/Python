import random
A=[]
for i in range(10):
    B=[]
    for j in range(8):
        b=random.randrange(0,99)
        B.append(b)

    A.append(B)
print(A)
print()
for i in range (10):
    for j in range (8):
        print("%6d" %A[i][j],end="")
    print()
for i in range (8):
