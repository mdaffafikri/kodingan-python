arr = input('masukin angka : ')

x = list(map(int, str(arr)))
print(x)

def urutin():
    output = [] 
    if sort == 'kecil':
        while x:
            terkecil = min(x)
            index = x.index(terkecil)
            output.append(x.pop(index))  

        print (output)

    elif sort == 'besar':
        while x:
            terbesar = max(x)
            index = x.index(terbesar)
            output.append(x.pop(index))

        print (output)

sort = input('dari besar atau kecil?')
urutin()