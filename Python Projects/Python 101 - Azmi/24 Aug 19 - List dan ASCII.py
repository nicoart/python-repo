# Latihan 17 August 2019
my_word = input("Input any word: ")
my_list = list(my_word)
print("The ASCII for each character in the word '" +  my_word + "' are:",end=" ")
for i in my_list:
    print(str(ord(i)),end=" ")
