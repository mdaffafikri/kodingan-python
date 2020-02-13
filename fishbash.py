jumlahangka = input('masukkan jumlah angka: ')

for i in range(1, int(jumlahangka)):
    if i % 15 == 0 :
        print('fishbash')
    
    elif i %5 == 0:
        print('bash')

    elif i % 3 == 0:
        print('fish')
    
    else :
        print(i)