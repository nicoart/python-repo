# Input bilangan yang akan dicari faktorial
num_input = int(input("Masukkan bilangan yang akan dicari nilai faktorialnya: "))

num = 1
faktorial = ""

for i in range(num_input,0,-1):
#    print(i)
    num *= i
    if faktorial == "":
        faktorial = str(i)
    else:
        faktorial = faktorial + " x " + str(i)

print("Faktorial dari",num_input,"adalah:",faktorial,"=",num)





