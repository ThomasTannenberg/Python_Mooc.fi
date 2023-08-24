# Write your solution here
def histogram(input_string):
    letter_counts = {}
    
    # Count letters
    for letter in input_string:

        if letter in letter_counts:
            letter_counts[letter] += 1
            #print('DEBUG:letter_counts_dictionary', letter_counts)
        else:
            letter_counts[letter] = 1
    
    # Print 
    for letter, count in letter_counts.items():
        number = '*' * count
        print(letter, number)


if __name__ == "__main__":
    histogram('abba')
    print('------')
    histogram("statistically")