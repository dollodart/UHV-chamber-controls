import u12
from funcs import PGA_auto

d=u12.U12(serialNumber=100054654)
for i in range(8,12):
    res=PGA_auto(d,i)
    print(res)
