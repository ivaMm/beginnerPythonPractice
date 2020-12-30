def check_row(lst):
    winner = 0
    for y in lst:
        if len(set(y)) == 1:
            winner = set(y).pop()
    return winner


def check_col(lst):
    col = list(zip(lst[0], lst[1], lst[2]))
    winner = 0
    for x in col:
        if len(set(x)) == 1:
            winner = set(x).pop()
    return winner


def check_diagonals(lst):
    d = [[lst[0][0], lst[1][1], lst[2][2]], [lst[0][2], lst[1][1], lst[2][0]]]
    winner = 0
    for x in d:
        if len(set(x)) == 1:
            winner = set(x).pop()
    return winner


def check_winner(lst):
    row = check_row(lst)
    col = check_col(lst)
    diagonals = check_diagonals(lst)
    if row > 0:
        print(f'Winner is player {row}!')
    if col > 0:
        print(f'Winner is player {col}!')
    if diagonals > 0:
        print(f'Winner is player {diagonals}!')


winner_is_2 = [[2, 0, 2], [1, 2, 0], [1, 1, 2]]
check_winner(winner_is_2)
