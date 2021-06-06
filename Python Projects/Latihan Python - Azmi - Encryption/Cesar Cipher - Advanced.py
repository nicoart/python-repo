# Latihan 17 August 2019
my_word = input("Input any words: ")
my_list = [ord(i) + 13 for i in list(my_word)]
print("Your encrypted words are",end=" ")
for i in my_list:
    if ((i >= 91 and i <= 103) or (i >= 123 and i <= 136)):
        i -= 26
    print(chr(i),end="")

