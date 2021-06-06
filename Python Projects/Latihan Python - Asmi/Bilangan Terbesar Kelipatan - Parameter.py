# Input bilangan yang akan dicari faktornya
num = int(input("Masukkan bilangan yang akan menjadi batas atas: "))
kelip = int(input("Kelipatan berapa? "))

kelipatan = num % kelip

if (kelipatan == 0):
    print("Nilai anda masukkan,",num,", adalah kelipatan",kelip)
else:
#    num -= kelipatan
    numbesar = num - kelipatan
    print("Kelipatan",kelip,"terbesar yang lebih kecil dari",num,"adalah",numbesar)