visitors = int(input("What is the number of visitors ?"))
if visitors>7:
    price=8*(visitors-1)
else:
    price=8*(visitors)
print("The price is :",price)
