# Write your solution here
def most_common_character(string):
    character_counts = {}
    for character in string:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1

    most_common_character = ""
    most_common_count = 0
    for character, count in character_counts.items():
        if count > most_common_count:
            most_common_character = character
            most_common_count = count

    return most_common_character


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))