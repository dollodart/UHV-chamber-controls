import u12

u12AES = u12.U12(serialNumber=100035035)
u12Cont = u12.U12(serialNumber=100054654)

print('cont')
for i in range(8):
    print(u12Cont.eAnalogIn(i))
print('AES')
for i in range(8):
    print(u12AES.eAnalogIn(i))
