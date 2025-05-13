min_time=99999999
    
for i in range (4):
    name_and_surname= input("What is your name and your surname ?")
    time = float(input("What was your time ?"))
    if (time<min_time):
        best_name_and_surname=name_and_surname
        min_time=time
print("The best athlete was",best_name_and_surname,"and his/hers time was ",min_time,"seconds")
    
