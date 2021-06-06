# Input bilangan yang akan dicari faktornya
num = int(input("Masukkan bilangan: "))

print("Faktor dari", num, "dan bilangan ganjil adalah:",end=" ")

for i in range(1, num):
    if (num % i == 0) and (i % 2 != 0):
        if (i != 1):
            print(",",end="")
        print(i,end="")

