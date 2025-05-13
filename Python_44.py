f=open('onomata.txt','r')
on=[]
for x in f:
    on.append(x[0:-1])
print(on)
f.close()
