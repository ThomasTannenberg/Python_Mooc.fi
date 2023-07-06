# Write your solution here
def ask_user():
    wage = float(input("what is the hourly wage?"))
    hours_worked = int(input("what are the hours worked?"))
    day = input("What is the day of the week?")
    return wage, hours_worked, day

def sunday_true(day):
    if day == "Sunday":
        return True
    else:
        return False

def daily_wages(wage, hours_worked, is_sunday):
    if is_sunday:
        daily_wages = wage * hours_worked * 2
    else:
        daily_wages = wage * hours_worked
    return daily_wages

def output(daily_wages):
    print("Daily wages:", daily_wages, "euros")

def main():
    wage, hours_worked, day = ask_user()
    is_sunday = sunday_true(day)
    daily_wage = daily_wages(wage, hours_worked, is_sunday)
    output(daily_wage)

main()


    
    