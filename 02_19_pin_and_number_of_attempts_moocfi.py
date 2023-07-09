
def input_code():
    code = int(input("PIN: "))
    return code

def check_code(counter):
    
    while True:
        code = input_code()
        counter += 1
        

        if code == 4321 and counter == 1:
            print("Correct! It only took you one single attempt!")
            break
        elif code == 4321:
            print("Correct! It took you", counter, "attempts")
            break
        else:
            print("Wrong")

def main():
    counter = 0
    check_code(counter)

main()
