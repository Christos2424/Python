import random
A=[]
for i in range(20):
    B=[]
    for j in range (7):
        players=random.randint(0,999)
        B.append(players)
    A.append(B)
print(A)
print()
for i in range (20):
    for j in range (7):
        print("%6d" %A[i][j],end="")   
    print()
        
for j in range (7):
    max=-1
    for i in range (20):
        if A[i][j]>max:
            max=A[i][j]
            th=i
    print (th+1)
