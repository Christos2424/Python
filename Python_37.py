def anazitisi(key,CODE=[]):
    for i in range(N):
        if key == CODE[i]:
            return (i)
    return (-1)
#====================MAIN=================================
CODE=[]
TIMI=[]
TEMA=[]
ESODA=[]
code = input('Give the code : ')
while code != 'ΤΕΛΟΣ':
    timi = input('Give the price of the product')
    tema = input('Give how many temaxia sold')
    TIMI.append(timi)
    CODE.append(code)
    TEMA.append(tema)
    code = input('Give the code : ')
N = len(CODE)

for i in range(len(CODE)):
    esoda = TIMI[i] * TEMA[i]
    ESODA.append(esoda)

for i in range(len(CODE)):
    print(CODE[i],TIMI[i],TEMA[i],ESODA[i])

key = input('Give code for search : ')
th = anazitisi(key.CODE)
if th == -1:
    print('Code doesnt exist')
else:
    print(ESODA[th])
    
    
    
    
    
