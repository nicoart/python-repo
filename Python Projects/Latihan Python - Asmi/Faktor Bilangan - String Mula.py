# Input bilangan yang akan dicari faktornya
num = int(input("Masukkan bilangan: "))

ganjil = ""
genap = ""
faktor = ""

for i in range(1, num):
    if (num % i == 0):
        if (i % 2 == 0):
            if genap == "":
                genap = str(i)
            else:
                genap = genap + "," + str(i)
        else:
            if ganjil == "":
                ganjil = str(i)
            else:
                ganjil = ganjil + "," + str(i)

print("Faktor dari", num, "dan bilangan genap adalah:",genap)
print("Faktor dari", num, "dan bilangan ganjil adalah:",ganjil)