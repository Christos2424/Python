def f1(people):
    if people <= 300:
        x = 8
    elif people <= 800:
        x = 12
    elif people <= 1500:
        x = 15
    else:
        x = 20
    return x
people = int(input("Give the number of people:"))
while people <= 0 or people > 2000:
    people = int(input("Give the number of people:"))
y = f1(people)
money = y * 50
print("You will pay :",money,"€")
