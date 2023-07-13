# Write your solution here
while True:
    user_input = input("Editor: ")

    if user_input.lower() == "visual studio code":
        print("an excellent choice!")
        break
    elif user_input.lower() == "notepad" or user_input.lower() == "word":
        print("awful")
    else:
        print("not good")

