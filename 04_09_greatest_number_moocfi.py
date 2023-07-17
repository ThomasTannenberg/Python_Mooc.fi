# Write your solution here
def greatest_number(number1, number2, number3):
    greatest = number1  
    if number2 > greatest:
        greatest = number2
    if number3 > greatest:
        greatest = number3
    return greatest

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, -100)
    print(greatest)