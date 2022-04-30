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

        # subtract the unicode of 'a' to get index in [0-25) range
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
