sum=0
temperature=float(input("What is the temperature of the sun in kelvin ? "))
while temperature!=0:
    if temperature==20000000:
        sum+=1
    temperature=float(input("What is the temperature of the sun in kelvin ? "))
print("The sum of the students that got the correct temperature are : ",sum)
