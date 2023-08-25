def largest(filename='numbers.txt') -> int:
    with open(filename, 'r') as new_file:
        contents = new_file.read()

    # Splitting the file content by newlines and converting each line to an integer.
    numbers = [int(num) for num in contents.split() if num.strip().isdigit()]
    
    # Return the largest number.
    return max(numbers) if numbers else None

if __name__ == "__main__":
    result = largest()  # Now you can call the function without any arguments
    
    if result is not None:
        print("The largest number is:", result)
    else:
        print("The file doesn't contain valid numbers.")


