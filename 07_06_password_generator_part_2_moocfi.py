from random import randint
import string

def generate_strong_password(length: int, numbers: bool, special: bool):
    alphabet_chars = string.ascii_lowercase
    number_chars = '0123456789'
    special_chars = '!?=+-()#'

    password_lst = []

    if numbers == False and special == False:
        for i in range(0, length):
            password_lst.append(alphabet_chars[randint(0, 25)])
    
    elif numbers == True and special == False:
        char_pool = alphabet_chars + number_chars
        password_lst.append(number_chars[randint(0, len(number_chars)-1)])
        for i in range(0, length-1):
            password_lst.append(char_pool[randint(0, len(char_pool)-1)])

    elif numbers == False and special == True:
        char_pool = alphabet_chars + special_chars
        password_lst.append(special_chars[randint(0, len(special_chars)-1)])
        for i in range(0, length-1):
            password_lst.append(char_pool[randint(0, len(char_pool)-1)])

    else:
        char_pool = alphabet_chars + number_chars + special_chars
        password_lst.append(number_chars[randint(0, len(number_chars)-1)])
        password_lst.append(special_chars[randint(0, len(special_chars)-1)])
        for i in range(0, length-2):
            password_lst.append(char_pool[randint(0, len(char_pool)-1)])

    return ''.join(password_lst)


if __name__ == '__main__':

    for i in range(10):
        print(generate_strong_password(8, True, True))
