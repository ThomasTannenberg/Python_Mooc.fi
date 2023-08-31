def print_diary():
    with open('diary.txt', 'r') as diary_file:
        print(diary_file.read())
#        for line in diary_file:
#            print(line)


def append_to_diary(user_input: str):
    with open('diary.txt', 'a') as diary_file:
        diary_file.write(user_input + '\n')

def main():

    while True:
        print('1 - add an entry, 2 - read entries, 0 - quiet')
        user_select = int(input('Function: '))

        if user_select == 1:
            diary_entry = input('Diary entry: ')
            append_to_diary(diary_entry)
            print('Diary saved')
        
        elif user_select == 2:
            print('Entries:')
            print_diary()
        
        elif user_select == 0:
            print('Bye now!')
            break

        else:
            print('wrong input')

main()




        