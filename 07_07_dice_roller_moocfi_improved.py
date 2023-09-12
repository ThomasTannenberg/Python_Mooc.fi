from random import choice

def roll(die: str):

    dice_dict = {
        'A' : [3, 3, 3, 3, 3, 6],
        'B' : [2, 2, 2, 5, 5, 5],
        'C' : [1, 4, 4, 4, 4, 4]
    }

    for die in dice_dict:
        return choice(dice_dict[die])

def play(die1: str, die2: str, times: int):
    dice_1_won = 0
    dice_2_won = 0
    dice_tie = 0

    for _ in range(times):
        dice_1_result = roll(die1)
        dice_2_result = roll(die2)

        if dice_1_result > dice_2_result:
            dice_1_won += 1
        elif dice_1_result < dice_2_result:
            dice_2_won += 1
        else:
            dice_tie += 1

    return dice_1_won, dice_2_won, dice_tie

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