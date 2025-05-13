import random
A=[]
for i in range (15):
    B=[]
    for j in range (12):
        kilos =random.randint(0,999)
        B.append(kilos)
    A.append(B)
print(A)
print()
for i in range (15):
    sum =0
    for j in range (12):
        print("%6d" %A[i][j],end="")
        sum +=A[i][j]
    print (" =",sum,end ="")
    print()

        
        
