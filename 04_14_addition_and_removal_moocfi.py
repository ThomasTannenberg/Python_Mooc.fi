# Write your solution here

def add_to_list(list):
    if len(list) == 0:
        list.append(1)
    else:
         last = list[-1]
         list.append(last + 1)
    return list

def remove(list):
    if len(list) == 0:
        print("the list is already empty")
    else:
        del list[-1]

def print_list(list):
        print(f"The list is now {list}")

def main():
    list = []
    print_list(list)

    while True:
        select = input("a(d)d, (r)emove or e(x)it:")
        if select == "d":
            add_to_list(list)
        elif select == "r":
            remove(list)
        elif select == "x":
            print("Bye!")
            break
        else:
            print("Can't do that. Select another option.")
        print_list(list)



main()


