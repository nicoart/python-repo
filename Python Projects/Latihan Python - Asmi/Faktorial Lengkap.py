x = 1
num_input = int(input("Masukkan bilangan yang akan dicari nilai faktorialnya: "))

print("Nilai faktorial dari",num_input,"= ",end='')
for i in range(1,num_input+1):
    x=x*i
    print(i,end='')
    if (i < num_input):
        print(" x ",end='')

print(" =",x)

