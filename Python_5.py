number = int(input("What is the number of the invited people : "))
if number <=500:
    price = number * 15
elif number <= 800:
    price = number * 13
elif number <= 1000:
    price = 10000
else :
    price = 10000 + 10*(number - 1000)
print("The price for the invited people wil be : ",price)
