# Write your solution here
def ask_user():
    temp_fahrenheit = int(input("Please give a temperature (F):"))
    return temp_fahrenheit

def convert_to_celsius(temp_fahrenheit):
    temp_celsius = float((temp_fahrenheit -32) * 5/9)
    return temp_celsius

def check_below_zero(temp_celsius):
    if temp_celsius < 0:
        print("Brr! It's cold in here!")

def output(temp_fahrenheit, temp_celsius):
    print(temp_fahrenheit, "degrees Fahrenheit equals", temp_celsius, "degrees Celsius")


def main():
    temp_fahrenheit = ask_user()
    temp_celsius = convert_to_celsius(temp_fahrenheit)
    output(temp_fahrenheit, temp_celsius)
    check_below_zero(temp_celsius)

main()