# Brute Force Attack - Decipher Cesar Cipher
print("This application is trying to decipher your secret sentence using Brute Force Attack")
my_word = input("Input your secret sentence: ")
trial_num = int(input("Number of suggested trial: "))
j = 0
while trial_num > 0:
    j += 1
    print("Trial no. " + str(j) + ":",end=" ")
    my_list = [ord(i) + j for i in list(my_word)]
    for i in my_list:
        if (i > 90 and i < 97) or (i > 122):
            i -= 26
        print(chr(i),end="")
    trial_num -= 1
    print("",end="\n")
