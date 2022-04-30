choice = ''
while choice != 'Q' or 'q':
    choice = input("Enter 'E' to encripte; 'D' to decripte; 'Esc' to exit the programme")
    if choice == 'E' or 'e':
        o_mes = 'abc'
        en_key = 5
        en_mes = ''

        for en_char in o_mes:
            if en_char.isupper():
                en_index = ord(en_char) - ord('A')
                en_shift = (en_index + en_key) % 26 + ord('A')
                en_range = chr(en_shift)
                en_mes += en_range
            elif en_char.islower():
                en_index = ord(en_char) - ord('a')
                en_shift = (en_index + en_key) % 26 + ord('a')
                en_range = chr(en_shift)
                en_mes += en_range
            elif en_char.isdigit():
                en_range = (int(en_char) + en_key) % 10
                en_mes += str(en_range)
            else:
                en_mes += en_char
        print("\n", o_mes + '\n', en_key, '\n', en_mes)
    elif choice == "D" or 'd':
        en_mes = 'fgh'
        de_key = 25
        num = 0
        de_mes = ''
        while de_key != -1:
            de_key = de_key - 1
            num = num + 1
            for de_char in en_mes:
                if de_char.isupper():
                    de_index = ord(de_char) - ord('A')
                    de_og_pos = (de_index - de_key) % 26 + ord('A')
                    de_og = chr(de_og_pos)
                    de_mes += de_og
                elif de_char.islower():
                    de_index = ord(de_char) - ord('a')
                    de_og_pos = (de_index - de_key) % 26 + ord('a')
                    de_og = chr(de_og_pos)
                    de_mes += de_og
                elif de_char.isdigit():
                    de_og = (int(de_char) - de_key) % 10
                    de_mes += str(de_og)
                else:
                    de_mes += de_char
            print('#', num, de_mes + "\n")
            de_mes = ''
    elif choice != 'Q' or 'q':
        print('faaf')
    else:
        break
