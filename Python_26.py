def f1():
    SO = str(input("Give your safety organization (Α,Β,Γ):"))
    while SO != 'Α' and SO != 'Β' and SO != 'Γ':
        SO = str(input("Give your safety organization (Α,Β,Γ):"))    
    if SO == 'Α':
        price = 30
    elif SO == 'B':
        price = 25
    else:
        price = 20
    return price
#============main==============
total = 0
onoma = str(input("Give your name:"))
while onoma!='ΤΕΛΟΣ': 
    price = f1()
    print("You will resive:",price,"€")
    onoma = str(input("Give your name:"))
    total += price
print("You resived in total",total,"€")

    
