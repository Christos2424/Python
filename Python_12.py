max_age=0
for i in range(5):
    name = input("What is your name ?")
    age = int(input("what is your age ?"))
    team = input("what is your team ?")
    if team == ("Γεράκι"):
        if (max_age < age):
            max_age = age
print("The oldest member of the γεράκι team is ",max_age,"years old")
