# Write your solution here
def dict_of_numbers():
    """Returns a dictionary with the numbers from 0 to 99 spelled out in words."""
    numbers = {}
    
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  
    
    for i in range(100):
        if i < 10:
            numbers[i] = ones[i]
        elif i < 20:
            numbers[i] = teens[i-10]
        else:
            if i % 10 == 0:
                numbers[i] = tens[i // 10]
            else:
                numbers[i] = tens[i // 10] + "-" + ones[i % 10]
                
    return numbers

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[0])
    print(numbers[1])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])