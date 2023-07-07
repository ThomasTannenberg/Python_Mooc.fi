
def ask_user():
    print("Person1:")
    name1 = input("Name: ")
    age1 = int(input("Age: "))

    print("Person2:")
    name2 = input("Name: ")
    age2 = int(input("Age: "))

    return name1, age1, name2, age2

def build_list(name1, age1, name2, age2):
    person1 = {"name": name1, "age": age1}
    person2 = {"name": name2, "age": age2}
    return person1, person2


def check_persons(person1, person2):
    return_name = ""
    if person1["age"] > person2["age"]:
        return_name = person1["name"]
        return return_name
    
    elif person2["age"] > person1["age"]:
        return_name = person2["name"]
        return return_name
    
    else:
        return_name is None

def output(return_name, name1, name2):
    if return_name is None:
        print(name1, "and", name2, "are the same age")
    else:
        print("The elder is", return_name)

def main():
    name1, age1, name2, age2 = ask_user()
    person1, person2 = build_list(name1, age1, name2, age2)
    return_name = check_persons(person1, person2)
    output(return_name, name1, name2)

main()



    



    