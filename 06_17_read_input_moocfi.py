def read_input(message: str, low_bound: int, high_bound: int):
    while True:
        try:
            number = int(input(message))
            if number >= low_bound and number <= high_bound:
                return number
        except ValueError:
            pass
        
        print(f'You must type in an integer between {low_bound} and {high_bound}')

if __name__ == "__'main'__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)