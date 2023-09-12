import random
import string

def generate_strong_password(length: int, numbers: bool, special: bool):
    alphabet_chars = string.ascii_lowercase
    number_chars = '0123456789'
    special_chars = '!?=+-()#'
    
    # Base char_pool
    char_pool = list(alphabet_chars)
    
    # Check for numbers and specials to be added
    if numbers:
        char_pool.extend(number_chars)
    if special:
        char_pool.extend(special_chars)

    # Ensure at least one number and special char if requested
    password_lst = []
    if numbers:
        password_lst.append(random.choice(number_chars))
    if special:
        password_lst.append(random.choice(special_chars))
    
    # Fill the rest of the password length with chars from char_pool
    for _ in range(length - len(password_lst)):
        password_lst.append(random.choice(char_pool))

    # Shuffle the password so that numbers/special chars are not just at the beginning
    random.shuffle(password_lst)

    return ''.join(password_lst)

if __name__ == '__main__':
    for i in range(10):
        print(generate_strong_password(8, True, True))
