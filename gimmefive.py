lima = False
num = input("Enter number : ")
print(list(num))

for x in range (len(num)):
    if(num[x]==str(5)):
        lima = True

def cetak():
    if(lima==True):
        print("found 5")
    else:
        print("5 not found")

cetak()