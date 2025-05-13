min_mo=9999
flag=False
min_on=' '
onoma=input("Give your name:")
while onoma !="Telos":
    flag=True
    bath1=float(input("Give the first grade :"))
    bath_max=bath1
    bath2=float(input("Give the second grade :"))
    if (bath2>bath_max):
        bath_max=bath2
    bath3=float(input("Give the third grade :"))
    if (bath3>bath_max):
        bath_max=bath3
    MO=(bath1+bath2+bath3)/3
    if (MO>=55)and(bath1>=50)and(bath2>=50)and(bath3>=50):
        print(onoma,"has passed with the grade of %.2f "%MO)
        if (MO<min_mo):
            min_mo=MO
            min_on=onoma
    print("The biggest grade was :",bath_max)
    onoma=input("Give your name :")
if (flag==False):
    print("The are no participants")
else:
     print(min_on,"had the lowest grade")

