# Kelipatan 3 terbesar yang lebih kecil dari suatu bilangan
num = int(input("Masukkan bilangan yang akan menjadi batas atas: "))
no_change = num

#kelipatan 3 terbesar
sisa_pembagian = num % 3

if (sisa_pembagian == 0):
    print("Nilai yang anda masukkan,",num,", adalah kelipatan 3")
else:
    num -= sisa_pembagian
#    num = num - sisa_pembagian
    print("Kelipatan 3 terbesar yang lebih kecil dari",no_change,"adalah",num)