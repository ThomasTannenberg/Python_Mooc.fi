def anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

if __name__ == "__main__":
    user_input1 = input("Please give the first word: ")
    user_input2 = input("Please give the second word: ")
    print(anagrams(user_input1, user_input2)) 

