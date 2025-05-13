price = int(input("What is the price of one pair of shoes ? "))
number = int(input("What is the number of the pairs ? "))
if number>18:
    number = number - 3
elif number>=10 and number<=18:
    number = number - 2
elif number>=5 and number<=9:
    number = number -1
money=price*number
print("The price of the shoes will be : ",money)
    
