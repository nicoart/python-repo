# Input bilangan yang akan dicari faktor persekutuan terbesarnya
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))

if num1 > num2:
    smaller = num2
    bigger = num1
else:
    smaller = num1
    bigger = num2

if (bigger % smaller == 0):
    fpb = smaller
else:
    for i in range(smaller,1,-1):
        if (smaller % i == 0) and (bigger % i == 0):
            fpb = i
            break
    else:
        fpb = 0

if (fpb != 0):
    print("Kelipatan Persekutuan Terbesar antara",bigger,"dan",smaller,"adalah:",fpb)
else:
    print(bigger,"dan",smaller,"tidak mempunyai Kelipatan Persekutuan Terbesar")


