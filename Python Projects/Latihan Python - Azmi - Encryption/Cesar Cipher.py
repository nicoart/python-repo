# Latihan 17 August 2019
my_word = input("Input any words: ")
my_list = [ord(i) - 3 for i in list(my_word)]
print("Your encrypted words are",end=" ")
for i in my_list:
    if (i < 65 or (i > 90 and i <97)):
        i += 26
    print(chr(i),end="")

