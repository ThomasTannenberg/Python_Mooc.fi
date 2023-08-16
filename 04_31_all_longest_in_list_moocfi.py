# Write your solution here
def all_the_longest(list):

  longest_string = ""
  longest_strings = []

  for string in list:
    if len(string) > len(longest_string):
      longest_string = string
      longest_strings = [string]

    elif len(string) == len(longest_string):
      longest_strings.append(string)

  return longest_strings


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)