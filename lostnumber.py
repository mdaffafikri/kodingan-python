a = [0,1,2,4,7,8,11]

def cek():
    for x in range(a[0], a[-1]+1):
        if x not in a:
            print("missing " + str(x))
        else: 
            pass
cek()