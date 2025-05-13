ONM = []
XRN = []
min_xr = 9999
min_nom = ''
for i in range(2):
    onm = str(input('Give the name of the athlete : '))
    xrn = float(input('Give the time of the athlete : '))
    ONM.append(onm)
    XRN.append(xrn)
    if (xrn<min_xr):
        min_xr = xrn
        min_nom = onm
print ('The fastest athlete was',min_nom,'with',min_xr,'s')   

