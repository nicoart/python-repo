my_word = input("Input any words: ").replace(" ","")
my_list = [ord(i) for i in list(my_word)]
my_list.sort()
print("Your encrypted word is",end=" ")
for i in my_list:
    print(chr(i),end="")

