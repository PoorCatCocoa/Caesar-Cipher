# The Encryption Function
# def encrypt(o_mes, en_key):
#fafafa

o_mes = 'abc'
en_key = 5
en_mes = ''

for en_char in o_mes:

    if en_char.isupper():  # check if it's an uppercase character

        en_index = ord(en_char) - ord('A')

        # shift the current character by key positions
        en_shift = (en_index + en_key) % 26 + ord('A')

        en_range = chr(en_shift)

        en_mes += en_range

    elif en_char.islower():  # check if its a lowecase character

        # subtract the unicode of 'a' to get index in [0-25) range
        en_index = ord(en_char) - ord('a')

        en_shift = (en_index + en_key) % 26 + ord('a')

        en_range = chr(en_shift)

        en_mes += en_range

    elif en_char.isdigit():

        # if it's a number,shift its actual value
        en_range = (int(en_char) + en_key) % 10

        en_mes += str(en_range)

    else:

        # if its neither alphabetical nor a number, just leave it like that
        en_mes += en_char
# return en_mes

print("\n", o_mes + '\n', en_key, '\n', en_mes)
