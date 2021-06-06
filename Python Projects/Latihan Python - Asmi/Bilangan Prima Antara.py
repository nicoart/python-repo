# Program python untuk menentukan bilangan prima lebih kecil dari bilangan yang diinputkan user
# Meminta input bilangan dari user
num = int(input("Masukkan bilangan: "))
# bilangan prima harus lebih besar dari 1
if num > 1:
    print("Bilangan Prima antara 2 dan", num, "adalah: ")
    for i in range(2,num):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
# bila bilangan kurang atau sama dengan satu
else:
    print(num, "bukan bilangan prima")