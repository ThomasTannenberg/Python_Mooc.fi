import json

def print_persons(filename: str):

    data = {}

    with open(filename, 'r') as file:
        data = json.load(file)

    #print(data)    

        for person in data:
            name = person['name']
            age = str(person['age'])
            hobbies = ', ' .join(person['hobbies'])
            
                

            print(f'{name} {age} years ({hobbies})')

if __name__ == '__main__':
    print_persons('file1.json')