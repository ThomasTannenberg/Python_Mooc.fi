def print_hashes(width, height):
    for i in range(0, height):
        print("#" * width)


def main():
    width = int(input("Width: "))
    height = int(input("Height: "))
    print_hashes(width, height)

main()