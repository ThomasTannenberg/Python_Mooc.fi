# Write your solution here

def is_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def next_leap_calc(year):
    next_year = year + 1
    while not is_leap(next_year):
        next_year += 1
    return next_year

def main():
    year = int(input("Year: "))
    next_leap_year = next_leap_calc(year)
    print("The next leap year after", year, "is", next_leap_year)

main()
