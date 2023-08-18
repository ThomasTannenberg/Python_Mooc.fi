# Write your solution here
def who_won(game_board: list):
    player_1_count = 0
    player_2_count = 0

    for row in game_board:
        for item in row:
            if item == 1:
                player_1_count += 1
            elif item == 2:
                player_2_count += 1

    if player_1_count > player_2_count:
        return 1
    elif player_2_count > player_1_count:
        return 2
    else:
        return 0



if __name__ == "__main__":

    list_game_stats = [
        [0, 1, 2, 1],
        [2, 2, 1, 0],
        [1, 0, 0, 0]
    ]

    print(who_won(list_game_stats))
    


