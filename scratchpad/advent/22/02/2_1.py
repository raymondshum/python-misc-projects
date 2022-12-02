from scratchpad.advent.utils.utils import Utils
from pprint import pprint
# Rock:     A, X
# Paper:    B, Y
# Scissors: C, Z

MOVE_NAME = {
    'A': 'ROCK',
    'X': 'ROCK',
    'B': 'PAPER',
    'Y': 'PAPER',
    'C': 'SCISSORS',
    'Z': 'SCISSORS'
}

POINTS_DICT = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}

WIN_DICT = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
    'Z': 'B',
    'X': 'C',
    'Y': 'A',
}

LOSE_DICT = {v: k for k,v in WIN_DICT.items()}

def main():
    file_path = r'C:\Users\rshum\Documents\CSUMB\Misc Projects\python\scratchpad\advent\22\02\input.txt'
    rounds = Utils.load_input(file_path)
    
    # player_score = 0
    # opponent_score = 0
    
    # for round_num, round in enumerate(rounds):
    #     opponent_move, player_task = round.split(" ")
    #     if WIN_DICT[opponent_move] == player_task:
    #         opponent_score += 6 + POINTS_DICT[opponent_move]
    #         player_score += POINTS_DICT[player_task]
    #         # print(f"R{round_num + 1} Player loses: +{POINTS_DICT[player_move]} | {player_score}")
    #     elif WIN_DICT[player_task] == opponent_move:
    #         player_score += 6 + POINTS_DICT[player_task]
    #         opponent_score += POINTS_DICT[opponent_move]
    #         # print(f"R{round_num + 1} Player wins: +6 + {POINTS_DICT[player_move]} | {player_score}")
    #     else:
    #         player_score += 3 + POINTS_DICT[player_task]
    #         opponent_score += 3 + POINTS_DICT[opponent_move]
    #         # print(f"R{round_num + 1} Player draws: +3 + {POINTS_DICT[player_move]} | {player_score}")
    
    # print("Player Score: ", player_score)
    
    player_score = 0
    opponent_score = 0
    for round_num, round in enumerate(rounds):
        opponent_move, player_task = round.split(" ")
        print(round, MOVE_NAME[opponent_move])
        if player_task == 'Z': # WIN
            player_move = LOSE_DICT[opponent_move]
            player_score += 6 + POINTS_DICT[player_move]
            opponent_score += POINTS_DICT[opponent_move]
            # print(f"R{round_num + 1} Player wins: 6 + {POINTS_DICT[player_move]} [{MOVE_NAME[player_move]}] | {player_score}")
        elif player_task == 'Y': # DRAW
            player_move = opponent_move
            player_score += 3 + POINTS_DICT[player_move]
            opponent_score += 3 + POINTS_DICT[opponent_move]
            # print(f"R{round_num + 1} Player draws: 3 + {POINTS_DICT[player_move]} [{MOVE_NAME[player_move]}] | {player_score}")
        elif player_task == 'X': # LOSE
            player_move = WIN_DICT[opponent_move]
            opponent_score += 6 + POINTS_DICT[opponent_move]
            player_score += POINTS_DICT[player_move]
            # print(f"R{round_num + 1} Player loses: +{POINTS_DICT[player_move]} [{MOVE_NAME[player_move]}] | {player_score}")
        else:
            raise ValueError("Invalid Player Task")    
    print("P2 Score: ", player_score)
if __name__ == "__main__":
    main()