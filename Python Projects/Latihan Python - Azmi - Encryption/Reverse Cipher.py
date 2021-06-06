# Latihan 14 September 2019
my_word = input("Input any words: ")
i = len(my_word) - 1
print("Your reversed encryption word(s) are",end=" ")
while i >= 0:
    print(my_word[i],end="")
    i -= 1

