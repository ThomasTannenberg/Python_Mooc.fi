# Write your solution here
def add_to_dict(file_name: str, finnish: str, english: str):
    with open(file_name, 'a') as file:
        file.write(finnish + ';' + english + '\n')
        print('Dictionary entry added')

def search_dict(file_name: str, search_term: str):
    with open(file_name) as file:
        for line in file:
            line = line.replace('\n', '')
            line = line.strip()
            words = line.split(';')
            finnish_word = words[0]
            english_word = words[1]
            
            if search_term in finnish_word or search_term in english_word:
                print(f'{finnish_word} - {english_word}')


def main():
    file_name = 'dictionary.txt'

    while True:
        print('1 - Add word, 2 - Search, 3 - Quit')
        user_input = int(input('Function: '))

        if user_input == 1:
            finnish_word = input('The word in Finnish: ')
            english_word = input('The word in Englisch: ')
            # implement add to dictionary function
            add_to_dict(file_name, finnish_word, english_word)
        elif user_input == 2:
            search_term = input('Search term: ')
            # implement search function and call it
            search_dict(file_name, search_term)
        elif user_input == 3:
            print('Bye!')
            break
        else:
            print('Wrong input, try again.')

main()