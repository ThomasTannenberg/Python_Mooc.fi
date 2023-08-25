# Write your solution here
def add_student(students: dict, name: str):
    students[name] = []
    return students


def print_student(students: dict, name: str):
    if name in students:
        if not students[name]: 
            print(f'{name}: \n no completed courses')
        else:
            print(f'{name} has completed the following courses: {", ".join(students[name])}')
    else:
        print(f'{name}: no such person in the database')

if __name__ == "__main__":

    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")