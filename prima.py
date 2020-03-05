n = int(input ("masukan n : "))
atas = int(input ("masukan max: "))

for x in range (n, atas):
    # print(x)
    prima = True
    for i in range (2, x):
        if (x%i == 0) :
            prima = False
    
    if prima == True :
        print(x, ' prima')
    else :
        print(x, ' gk prima')
