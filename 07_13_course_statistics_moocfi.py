# Write your solution here
import urllib.request
import json

def retrieve_all():
    json_data = json.load(urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses"))
    #print(json_data)

    printout_list = []


    for course in json_data:
        if course['enabled'] == True:
            course_name = course['fullName']
            name = course['name']
            year = course['year']
            exercises_sum = sum(course['exercises'])

            to_list = (course_name, name, year, exercises_sum)

            printout_list.append(to_list)
    
    return printout_list

def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = my_request.read()
    course = json.loads(data)

    course_info = {}
    weeks = 0
    students = 0
    hours = 0
    exercises = 0
    for week, data in course.items():
        weeks += 1
        if data['students'] > students:
            students = data['students']
        hours += data['hour_total']
        exercises += data['exercise_total']
    hours_average = int(hours/students)
    exercises_average = int(exercises/students)

    course_info['weeks'] = weeks
    course_info['students'] = students
    course_info['hours'] = hours
    course_info['hours_average'] = hours_average
    course_info['exercises'] = exercises
    course_info['exercises_average'] = exercises_average

    return course_info

if __name__ == '__main__':
    print(retrieve_all())

    retrieve_course('docker2019')