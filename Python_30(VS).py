A = []
sum = 0
for i in range(10):
    a = int(input('Δώσε τον αριθμό τον αυγών : '))
    A.append(a)
    sum += a
print (sum,sum/10)
for i in range(10):
    if A[i]>sum/10:
        print('Η παραγωγή ξεπέρασε τον μέσο όρο την ',i+1,'μέρα')
    
