# Input bilangan yang akan dicari faktorial
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))
bil3 = int(input("Masukkan bilangan ketiga: "))

if bil1 >= bil2:
    if bil1 >= bil3:
        terbesar = bil1
    elif bil1 < bil3:
        terbesar = bil3
