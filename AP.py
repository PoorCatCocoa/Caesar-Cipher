# One way to using Caesar Cipher for encrypt & force decrypt.
print("This is a program using Caesar-Cipher to encrypt messages, "
      "please read the instructions clearly"+"\n\n")  # introduction
choice = ''  # variable for recording user choice
collect = []  # list for collecting encryption data
while True:  # while loop for the whole program
    choice = input("\nEnter 'E' to encrypt; 'D' to decrypt; "
                   "'C' to show the collect data;'Q' to quit the programme")  # user menu
    if choice == 'E' or choice == 'e':  # encrypt part
        o_mes = input("\nEnter the message need to encrypt: ")  # original message user input
        en_key = int(input("\nEnter an number between '1-25': "))  # the key user input for encrypt
        en_mes = ''  # the variable for encrypted message
        for en_char in o_mes:  # read characters in user input
            if en_char.isupper():  # check capital
                en_index = ord(en_char) - ord('A')
                en_shift = (en_index + en_key) % 26 + ord('A')
                en_range = chr(en_shift)
                en_mes += en_range
            elif en_char.islower():  # check lower case
                en_index = ord(en_char) - ord('a')
                en_shift = (en_index + en_key) % 26 + ord('a')
                en_range = chr(en_shift)
                en_mes += en_range
            elif en_char.isdigit():  # check numbers
                en_range = (int(en_char) + en_key) % 10
                en_mes += str(en_range)
            else:
                en_mes += en_char  # check symbols
        print("\nThe 'original message' & the 'key you entered' & the 'encrypted message' "
              "is shown below:" + '\n', o_mes + '\n', en_key, '\n', en_mes)  # output for encrypt
        collect = [o_mes, en_key, en_mes] # collect encrypt data
    elif choice == "D" or choice == 'd':  # decrypt part
        en_mes = input("Enter the message need to decrypt: ")  # encrypted message user input
        de_key = 25  # try all chance for decrypt
        num = 0  # counting
        de_mes = ''  # variable for decrypted message
        print('The decrypted messages are shown below: ')  # output remind
        while de_key != -1:  # checking the total shift time
            de_key = de_key - 1  # auto discount for left shift time
            num = num + 1  # counting
            for de_char in en_mes:  # read characters in user input
                if de_char.isupper():  # check capital
                    de_index = ord(de_char) - ord('A')
                    de_og_pos = (de_index - de_key) % 26 + ord('A')
                    de_og = chr(de_og_pos)
                    de_mes += de_og
                elif de_char.islower():  # check lower case
                    de_index = ord(de_char) - ord('a')
                    de_og_pos = (de_index - de_key) % 26 + ord('a')
                    de_og = chr(de_og_pos)
                    de_mes += de_og
                elif de_char.isdigit():  # check numbers
                    de_og = (int(de_char) - de_key) % 10
                    de_mes += str(de_og)
                else:
                    de_mes += de_char  # check symbols
            print('No.', num, de_mes + "\n")  # output for decrypted messages
            de_mes = ''  # refresh
    elif choice == 'C' or choice == 'c':  # data collecting part
        print("The data collected shown below: ", collect)  # data output
    elif choice == 'Q' or choice == 'q':  # quit the program
        quit("! PROGRAM END !")
    else:  # if user typing unknown command
        print('\n! You have entered an invalid input !\n')
