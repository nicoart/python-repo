# Input bilangan yang akan dicari faktornya
num = int(input("Masukkan bilangan: "))

print("Faktor dari", num, "adalah:")
for i in range(1, num):
    if num % i == 0:
        print(i)
