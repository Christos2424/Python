epitheto1 = (input("Give your surname :"))
onoma1 = (input("Give your name :"))
bathmos1 = int(input("Give your grade :"))
print()
epitheto2 = (input("Give your surname :"))
onoma2 = (input("Give your name :"))
bathmos2 = int(input("Give your grade :"))
print()
epitheto3 = (input("Give your surname :"))
onoma3 = (input("Give your name :"))
bathmos3 = int(input("Give your grade :"))
print()
if bathmos1<bathmos2<bathmos3:
    bathmosmax=bathmos3                     
    onomamax=onoma3
    epithetomax=epitheto3
elif bathmos1>bathmos2>bathmos3:
    bathmosmax=bathmos1
    onomamax=onoma1
    epithetomax=epitheto1
elif bathmos1<bathmos2>bathmos3:
    bathmosmax=bathmos2
    onomamax=onoma2
    epithetomax=epitheto2
print("The student with the best grade is :",onomamax,"Their surname is : ",epithetomax,"Their grade is :",bathmosmax)
    
    
