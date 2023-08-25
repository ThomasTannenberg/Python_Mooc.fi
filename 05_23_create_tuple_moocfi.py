# Write your solution here
def create_tuple(x: int, y: int, z: int):
    list = [x, y, z]
    list.sort()

    first_val = list[0]
    second_val = list[2]
    third_val = sum(list)

    tuple = (first_val, second_val, third_val)

    return tuple






if __name__ == "__main__":
#    create_tuple(5, 3, -1)
    print(create_tuple(5, 3, -1))