from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):
    rnd_list = []

    while len(rnd_list) < amount:
        rnd_number = randint(lower, upper)
        
        if rnd_number not in rnd_list:
            rnd_list.append(rnd_number)
    
    rnd_list.sort()
    return rnd_list

if __name__ == '__main__':
    for number in lottery_numbers(7, 1, 40):
        print(number)