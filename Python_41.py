import random
A=[]
ON=[]
for i in range(3):
    B=[]
    on=input("Give a name")
    ON.append(on)
    for j in range(5):
        b=random.randint(0,99)
        B.append(b)
    A.append(B)
max=-1
for i in range (3):
    sum = 0
    for j in range(5):
        sum += A[i][j]
    if sum > max:
        max=sum
        maxName=ON[i]
print(maxName, max)
        
        
