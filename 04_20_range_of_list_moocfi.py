# Write your solution here
def range_of_list(list):
    min_wert = min(list)
    max_wert = max(list)
    return max_wert - min_wert



# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)