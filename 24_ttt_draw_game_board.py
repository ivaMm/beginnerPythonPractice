def draw_board(row, col):
    if row <= 0 or col <= 0:
        return False
    else:
        col1 = '|   ' * (col+1)
        col2 = ' ---' * col + '\n'
        col = col2 + col1 + '\n'
        print(col * row + col2)


def draw_it():
    print('What size game board you want to draw?')
    row = int(input('Rows: '))
    col = int(input('Columns: '))
    return draw_board(row, col)


draw_it()
