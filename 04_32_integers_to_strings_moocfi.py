# Write your solution here
def formatted(list):
    new_list = []
    for word in list:
        new_list.append(f"{word:.2f}")
    
    return new_list

if __name__ == "__main__":
    my_list = [1.234, 0.333, 0.11111, 3.466]
    new_list = formatted(my_list)
    print(new_list)