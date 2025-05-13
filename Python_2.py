xr = int(input("Συνολικά χρήματα : "))
MK = int(input("Μέρες Κωστίκα : "))
MG = int(input("Μέρες Γιωρίκα : "))
day = xr/(MK+MG)
xrg = MG * day
xrk = MK * day
print("Γιωρίκας : ",xrg,"Κωστίκας : ",xrk)
