from random import randint

def roll(die: str):
    dice_a = [3, 3, 3, 3, 3, 6]
    dice_b = [2, 2, 2, 5, 5, 5]
    dice_c = [1, 4, 4, 4, 4, 4]

    if die == 'A':
        return dice_a[randint(0, len(dice_a)-1)]
    elif die == 'B':
        return dice_b[randint(0, len(dice_b)-1)]
    elif die == 'C':
        return dice_c[randint(0, len(dice_c)-1)]

def play(die1: str, die2: str, times: int):
    dice_1_result = 0
    dice_2_result = 0

    dice_1_won = 0
    dice_2_won = 0
    dice_tie = 0

    for i in range(times):
        dice_1_result = roll(die1)
        dice_2_result = roll(die2)

        if dice_1_result > dice_2_result:
            dice_1_won += 1
        elif dice_1_result < dice_2_result:
            dice_2_won += 1
        else:
            dice_tie += 1
    
    return (dice_1_won, dice_2_won, dice_tie)




if __name__ == '__main__':
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    

    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)