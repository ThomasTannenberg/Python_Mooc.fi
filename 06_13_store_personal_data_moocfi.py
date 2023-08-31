# Write your solution here
def store_personal_data(person: tuple):
    person_list = []

    with open('people.csv', 'w') as new_file:
        person_list.append(person[0])
        person_list.append(str(person[1]))
        person_list.append(str(person[2]))
        line = ';'.join(person_list) + '\n'
        new_file.write(line)


if __name__ == "__main__":
    test_tuple = ('Paul Paulson', 37, 175.5)
    store_personal_data(test_tuple)
    #store_personal_data('Thomas Tannenberg', 40, 181.2)




