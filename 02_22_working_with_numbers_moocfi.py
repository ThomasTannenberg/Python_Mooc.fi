def get_numbers():
    number = int(input("Number: "))
    return number

def output():
    counter = 0
    numbers = []
    negatives = []
    positives =[]

    while True:

        number = get_numbers()
        counter += 1

        if number == 0:
            total = sum(numbers)
            mean = total / len(numbers)
            amt_negatives = len(negatives)
            amt_positives = len(positives)
            
            print("Numbers typed in", counter - 1)
            print("The sum of the numbers is", total)
            print("The mean of the numbers is", mean)
            print("Positive numbers", amt_positives)
            print("Negative numbers", amt_negatives)

            break
        else:
            numbers.append(number)

            if number > 0:
                positives.append(number)
            elif number < 0:
                negatives.append(number)
          
def main():
    print("Please type in integer numbers. Type in 0 to finish.")
    output()

main()
