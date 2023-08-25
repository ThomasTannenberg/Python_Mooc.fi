# Write your solution here

def invert(dictionary: dict):
    dict_temp = {}
    for key, value in dictionary.items():
        dict_temp[value] = key
    
    dictionary.clear()
    dictionary.update(dict_temp)



if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)