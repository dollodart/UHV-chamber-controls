#nominal manufacturer conversion:
#T = (V0-1.25 V)/(0.005 V)

# see thermocouple voltage T(V) polynomials in standard references
Tmin,Tmax=[0.,1200.]
vmin,vmax=[0.005*Tmin+1.25,0.005*Tmax+1.25]
print(vmin,vmax)
