sum_old=0
sum_young=0
age=float(input("What is the age of the lion ? "))
while age>0 :
    if (age>=10):
        sum_old+=1
    if (age<=4):
        sum_young+=1
    age=float(input("What is the age of the lion ? "))
print("The lions older or 10 year old are : ",sum_old,"and the lions younger or 4 year old are : ",sum_young)

        
        
