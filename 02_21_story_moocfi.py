def get_words():

    words = []
    previous_word = None

    while True:
        word = input("Please type in a word: ")
        if word == "end":
            break
        elif word == previous_word:
            break
        else:
            words.append(word)
            previous_word = word

    return words

def generate_story(words):
    story = " ".join(words)
    return story

def main():

    words = get_words()
    story = generate_story(words)
    print(story)

main()

