# Copy here code of line function from previous exercise
def line(number, string):

    if string == "":
        print(number * "*")
    else:
        print(number * string[0])

def triangle(size):
    for i in range(1, size + 1):
        line(i, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
