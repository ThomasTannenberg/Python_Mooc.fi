# function to read file
def read_file(file_name):
    with open(file_name) as file:                                  # open file as stream

        dict = {}                                                  # intilaize dictionary to save values

        for line in file:                                          # goes through the file line by line
            line = line.replace('\n', '')                          # filters out line breaks
            line_as_list = line.split(';')                         # creates new list. Items are recognized by ';'

            if line_as_list[0] == 'id':                            # skips the first line in the CSV. It cannot be processed
                continue
            dict[line_as_list[0]] = line_as_list[1:]               # creates dictionary

    return dict                                                    # returns dictionary

# Convert list of strings to list of ints in place
def list_str_to_int(list):
    for index, value in enumerate(list):
        list[index] = int(value)

def main():
    # For DEBUGGING to skip annoying input. 
    if True:                                                        # set FALSE for DEBUGGING and TRUE for final code
        student_file = input('Student information: ')
        exercises_file = input('Exercises completed: ')
    else:
        student_file = 'students1.csv'
        exercises_file = 'exercises1.csv'
    
    students = read_file(student_file)
    exercises = read_file(exercises_file)

    # Dictionary exercises has list of strings as value. Convert list of strings to list of ints
    for id, exercises_list in exercises.items():
        list_str_to_int(exercises_list)
    
    for id, name in students.items():
        exercises_total = sum(exercises[id])
        print(f'{name[0]} {name[1]} {exercises_total}')

main()
                                
        