# Write your solution here
def shortest(list):
    shortest_word = list[0]
    for word in list:
        if len(word) < len(shortest_word):
            shortest_word = word
    
    return shortest_word

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)