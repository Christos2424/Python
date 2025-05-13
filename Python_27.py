def place(mo):
    if mo < 13.5:
        return 'Γ4'
    elif mo < 16:
        return 'Γ3'
    elif mo < 18.5:
        return'Γ2'
    elif mo <= 20:
        return'Γ1'
#==================main============================
math_g1 = 0
math_g2 = 0
math = 1
math_g3 = 0
while math <= 30 or math_g1 <= 4:
    on = input("Give your name:")
    mo = int(input("Give your meso oro:"))
    while mo >= 9.5 and mo <= 20:
        tm = place(mo)
        if tm == 'Γ1':
            math_g1 += 1
        elif tm == 'Γ2':
            math_g2 += 1
        if mo >= 17 and mo <= 19: 
            math_g3 += 1
        print(on,"you are in",tm)   
        on = input("Give your name:")
        mo = int(input("Give your meso oro:"))
        math += 1
print("Number of students in Γ2 are:",math_g2)
print("The percentage of students between mo 17 to 19 is",(math_g3/math)*100,"%")        
    
     

         
