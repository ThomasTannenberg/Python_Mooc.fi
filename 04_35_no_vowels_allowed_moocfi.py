# Write your solution here
def no_vowels(string):
    formated_string = ""
    vowells = "aeiou"
    for char in string:
        if char not in vowells:
            formated_string = formated_string + char

    return formated_string

if __name__ == "__main__":
    my_string = "This is an example"
    print(no_vowels(my_string))