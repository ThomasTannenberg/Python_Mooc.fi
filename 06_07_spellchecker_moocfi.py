def read_file(file_name):

    list_with_words = []

    with open(file_name) as word_list:

        for line in word_list:
            line = line.replace('\n', '')
            list_with_words.append(line)
    
    return list_with_words

def main():
    word_input = input('Write text: ')

    word_input_list = word_input.split(' ')

    correct_words = read_file('wordlist.txt')

    for index, word in enumerate(correct_words):
        correct_words[index] = word.lower()
    output = ''

    for text in word_input_list:
        if text.lower() in correct_words:
            output += text
        else:
            output += '*' + text + '*'
        output += ' '
    
    print(output)


main()


