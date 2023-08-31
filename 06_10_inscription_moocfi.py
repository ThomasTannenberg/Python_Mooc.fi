# Write your solution here
def user_input():
    name = input('Whom should I sign this to: ')
    file_name = input('Where shall I save it: ')

    return name, file_name

def file_write(name: str, file_name: str):
    with open(file_name, 'w') as new_txt:
        new_txt.write(f'Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team')

def main():
    name, file_name = user_input()
    file_write(name, file_name)
    
main()