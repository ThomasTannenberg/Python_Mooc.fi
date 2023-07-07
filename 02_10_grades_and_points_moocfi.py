
def calculate_grade(points):
    if points < 0:
        grade = "impossible!"
    elif points <= 49:
        grade = "fail"
    elif points <= 59:
        grade = "1"
    elif points <= 69:
        grade = "2"
    elif points <= 79:
        grade = "3"
    elif points <= 89:
        grade = "4"
    elif points <= 100:
        grade = "5"
    else:
        grade = "impossible!"

    return grade

def main():
    points = int(input("How many points [0-100]: "))
    grade = calculate_grade(points)
    print("Grade:", grade)

main()
