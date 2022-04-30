# 用中文给你注释一遍，你到时候自己翻译一下
de_key = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ').encode()  # 这是密码的源码
en_key = ('t3JHWXLoOeKAVbjC6TYsEPD9zd SpxMg5ilwRm07yFu8rkZq1cNnfaGUhQIBv24').encode()  # 这是打乱的密码

de_list = bytes.maketrans(en_key, de_key)  # 这是解码用的list
en_list = bytes.maketrans(de_key, en_key)  # 这是加密用的list

# 三个变量，名字不喜欢的话可以改
result = ''
choice = ''
message = ''

while choice != 'q' or 'Q':  # while循环，判定按键是否按下
    choice = input(
        "\n Do you want to encrypt or decrypt the message?\n Enter 'E' to encrypt, 'D' to decrypt or 'Q' to exit.")  # 用户输入

    if choice == 'e' or 'E':  # if循环，判定按键是否按下
        message = input('\nEnter message for encryption: \n')  # 用户输入
        result = message.translate(en_list)  # 加密区
        print('\n', result, '\n\n')  # 输出

    elif choice == 'd' or 'D':  # elif检测，判定按键是否按下
        message = input('\nEnter message for decrypt: ')  # 用户输入
        result = message.translate(de_list)  # 解码区
        print('\n', result, '\n\n')  # 输出

    elif choice != 'q' or 'Q':  # elif检测，判定按键是否按下
        print('! You have entered an invalid input, please try again. !\n\n')  # 输出

    else:  # 避免bug情况发生，确保中断循环
        break
