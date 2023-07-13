# Write your solution here
def chessboard(length):
    for zeile in range(length):
        for spalte in range(length):
            if (zeile + spalte) % 2 == 0:
                print("1", end="")
            else:
                print("0", end="")
        print()


# Testing the function
if __name__ == "__main__":
    chessboard(3)
