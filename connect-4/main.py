"""

"""

import os

PIECES = ("X", "O")
GRID_WIDTH = 6
GRID_HEIGHT = 7

def populate_row(width: int) -> list[str]:
    row = []
    for idx in range(width):
        row.append("")
    return row


def draw_row(row: list[str]) -> None:
    formatted_row = []

    for string in row:
        if string == "":
            formatted_row.append("." + " |")
        else:
            formatted_row.append(string + " |")
    
    print("| " + ' '.join(formatted_row))


def generate_grid(width: int, height: int) -> list[list[str]]:
    rows = []
    for row in range(height):
        rows.append(populate_row(width))
    return rows


def add_row_lines(row: list[str]) -> None:
    line = []
    for string in row:
        line.append("----")
    
    print("-" + "".join(line))


def draw_grid(grid: list[list[str]]) -> None:
    for idx in range(len(grid)):
        draw_row(grid[idx])
        add_row_lines(grid[idx])

grid = generate_grid(width=GRID_WIDTH, height=GRID_HEIGHT)

def check_if_position_populated(grid: list[list[str]], position: int, row: int) -> bool:
    return "X" in grid[row][position-1] or "O" in grid[row][position-1]


def insert_piece_into_grid(grid: list[list[str]], piece: str, position: int) -> list[list[str]]:
    for idx, row in enumerate(grid):
        is_position_populated = check_if_position_populated(grid, position, -(idx+1))

        if is_position_populated:
            continue
        else:
            grid[-(idx+1)][position-1] = piece
            break
    return grid


def player_turn(grid: list[list[str]], piece: str) -> int:
    position = int(input("Pick a position: "))
    insert_piece_into_grid(grid, piece, position)
    return position


def format_player_name(name: str) -> str:
    new_name = " ".join(name.split("_")).title()
    return new_name


def check_win_on_axis(axis: list[str]) -> bool:
    chained_piece_count = 1
    for idx, square in enumerate(axis):
        if square == ".":
            continue
        if idx == 0:
            continue
        if axis[idx] == axis[idx-1]:
            chained_piece_count += 1
        else:
            chained_piece_count = 1
        if chained_piece_count == 4:
            return True
    return False


def get_individual_column(grid: list[list[str]], column_position: int) -> list[str]:
        return [row[column_position] for row in grid]


def get_columns(grid: list[list[str]]) -> list[list[str]]:
    grid_width = len(grid[0])
    columns = []
    for column_position in range(grid_width):
        column = get_individual_column(grid, column_position)
        columns.append(column)
    return columns


def check_win(grid: list[list[str]]) -> bool:
    for row in grid:
        is_row_win = check_win_on_axis(row)
        if is_row_win:
            return True
    columns = get_columns(grid)
    for column in columns:
        print(column)
        is_column_win = check_win_on_axis(column)
        if is_column_win:
            return True
    return False


def check_diagonal_win_from_left_side(grid: list[list[str]]) -> bool:
    chained_piece_count = 1
    for row_idx, row in enumerate(grid):
        for square_idx, square in enumerate(row):
            if square == ".":
                continue
#            print(row)
            if square == grid[row_idx-1][square_idx-1]:
#                print("----CHAINED PIECE----")
                chained_piece_count += 1
            else:
                chained_piece_count = 1
#            print(f"piece = {square}, idx = {square_idx}, chained pieces = {chained_piece_count}\n")
            if chained_piece_count == 4:
                return True
    return False

def check_diagonal_win_from_right_side(grid: list[list[str]]) -> bool:
    chained_piece_count = 1
    for row_idx, row in enumerate(grid):
        for square_idx, square in enumerate(row):
            if square == ".":
                continue
            if row[square_idx] == row[-1]:
                continue
#            print(row)
            if square == grid[row_idx-1][square_idx+1]:
#                print("----CHAINED PIECE----")
                chained_piece_count += 1
            else:
                chained_piece_count = 1
#            print(f"piece = {square}, idx = {square_idx}, chained pieces = {chained_piece_count}\n")
            if chained_piece_count == 4:
                return True
    return False

def play_game():
    os.system("clear")
    draw_grid(grid)
    while True:
        for player_number, piece in enumerate(PIECES):
            print(f"Player {player_number}'s turn: ({piece})")
            player_turn(grid, piece)
            os.system("clear")
            draw_grid(grid)
            is_won_1 = check_win(grid)
            is_won_2 = check_diagonal_win_from_left_side(grid)
            is_won_3 = check_diagonal_win_from_right_side(grid)
            print(is_won_1, is_won_2, is_won_3)

#def play_game():
#    os.system("clear")
#    draw_grid(grid)
#    while True:
#        for player_number, piece in enumerate(PIECES):
#            print(f"Player {player_number}'s turn: ({piece})")
#            player_turn(grid, piece)
#            os.system("clear")
#            draw_grid(grid)
#            is_won_1 = check_win(grid)
#            is_won_2 = check_diagonal_win_from_left_side(grid)
#            is_won_3 = check_diagonal_win_from_right_side(grid)
#            print(is_won_1, is_won_2, is_won_3)


if __name__ == "__main__":
    play_game()

