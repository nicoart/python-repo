ArrNamaBali = ["WAYAN", "PUTU", "GEDE", "MADE", "KADEK", "NYOMAN", "KOMANG", "KETUT"]
print("Program Sederhana 1 - Tebak Orang Bali atau Bukan")

#NamaAnda= input("\nMasukkan Nama Lengkap anda, pisahkan dengan spasi untuk tiap kata: ")
#word = "Hello"
#print(word.find("o"))

NamaPertama = input("\nMasukkan Nama Pertama anda: ")
NamaKedua = input("Masukkan Nama Kedua dan Ketiga ada (bila ada), pisahkan dengan spasi: ")
#print(NamaPertama.upper())
if NamaPertama.upper() not in ArrNamaBali:
    print("\n" + NamaPertama + " " + NamaKedua + ", anda bukan orang Bali")
else:
    print("\n" + NamaPertama + " " + NamaKedua + ", anda orang Bali")