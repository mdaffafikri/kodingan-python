tulisan = input('masukan tulisan : ')

listtulisan = list(tulisan)

dibalik = []

for i in reversed(listtulisan):
    dibalik.append(i)

jadistring = ''.join(dibalik)

print(jadistring)
print(tulisan)

if jadistring == tulisan:
    print(True)

else:
    print(False)
    
    


