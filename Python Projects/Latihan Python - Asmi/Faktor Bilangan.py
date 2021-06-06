# Input bilangan yang akan dicari faktornya
num = int(input("Masukkan bilangan: "))

factor = []
odd = []
even = []


for i in range(1, num):
    if (num % i == 0):
        factor.append(i)
        if (i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)

print("Faktor dari", num, "adalah: ",end="")
print(*factor,sep = ',')

print("Faktor dari", num, "dan genap adalah: ",end="")
print(*even,sep = ',')

print("Faktor dari", num, "dan ganjil adalah: ",end="")
print(*odd,sep = ',')
