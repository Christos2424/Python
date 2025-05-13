max = -1
for i in range (5):
    onoma = input('Give a name:')
    if len(onoma) > max:
        max = len(onoma)
        max_on = onoma  
print ('The longest name is',max_on)
