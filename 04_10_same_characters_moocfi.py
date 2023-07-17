# Write your solution here
def same_chars(word, index1, index2):
    if index1 >= 0 and index1 < len(word) and index2 >= 0 and index2 < len(word):
        if word[index1] == word[index2]:
            return True
    return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))