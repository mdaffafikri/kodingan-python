import statistics

#a, b = input('masukan a dan b = ')
tuple1 = (1,2,3,4,5,6,7)

list1=[]

def debug():
 print("debug")

def ngelist(n):
    i = 1
    while i <= n:
        list1.append(i)
        i+=1
    return print(list1)

n = int(input ("masukan n : "))

ngelist(n)
mid = (statistics.median(list1))
print("nilai tengah = " + str(mid))

#print ("{:.2f}".format(mid))
#print(statistics.median(tuple1))