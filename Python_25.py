def shoes(shoe,price):
    if shoe > 18:
        m = (shoe - 3) * price
    elif shoe >=10:
        m = (shoe - 2) * price
    elif shoe >=5:
        m = (shoe - 1) * price
    else:
        m = shoe * price
    return m
#====================main========================
shoe = int(input("Give number of shoes:"))
price = float(input("Give the price of the shoe:"))
m = shoes(shoe,price)
print("You will pay: ",m)

    
    
