full=0
for i in range (1,26):
    passengers=int(input("Number of passengers:"))
    print('The number of passengers are:',passengers)
    if (passengers==350):
        full = full + 1
percent = (full/25*100)
print ("The train has reached its full capacity ",percent,"% of the time")


