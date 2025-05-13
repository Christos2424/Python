MP = []
for i in range(30):
    mp = int(input('Αριθμός μπουκαλιών :'))
    MP.append(mp)    
    sum += mp 
print (sum,sum/30)
sum1 = 0
for i in range(15):
    sum += MP[i]
sum2 = 0
for i in range(15,30,1):
    sum2 += MP[i]

if sum1>sum2:
    print ('first')
elif sum2>sum1:
    print ('second')
else:

