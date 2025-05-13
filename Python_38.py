import random
A=[]
for i in range(5):
    B=[]
    for j in range (20):
        b = random.randint(0,99)
        B.append(b)
        
    A.append(B)
print(A)
print()
for i in range (5):
    for j in range (20):
        print("%6d" %A[i][j],end="")
    print()
for i in range (5):
    sum = 0
    for j in range (20):
        sum += A[i][j]
    print(sum)

    
