L = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
word = input('Give a word:')
m1 = 0
for x in word:
    if x in L:
        m1 += 1
if len(word) == m1:
    print('Είναι όλα κεγαλαία')
else:
    print('Δεν είναι όλα κεφαλαία')
    
    

        
