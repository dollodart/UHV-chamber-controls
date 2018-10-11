import u12

d1 = u12.U12(serialNumber=100054654)
d2 = u12.U12(serialNumber=100035035)

print('d1')
for i in range(8):
    print(d1.eAnalogIn(i))
print('d2')
for i in range(8):
    print(d2.eAnalogIn(i))
