"""

"""

import os

PIECES = ("X", "O")
GRID_WIDTH = 6
GRID_HEIGHT = 7
def populate_row(width: int) -> list[str]:
    row = []
    for idx in range(width):
        row.append(".")
    return row


def draw_row(row: list[str]) -> None:
    formatted_row = []

    for string in row:
        if string == ".":
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

grid = [[".",".",".",".",".","."],
        [".",".",".",".",".","."], 
        [".","X",".",".",".","."], 
        [".",".","X","O",".","."],
        [".",".","X",".",".","."],
        ["X","O","O","X","X","."],
        ["X","X","X","O","X","X"]]


def calculate_rows_to_skip(grid:list[list[str]]) -> int:
    rows_skipped = 0
    for internal_row_idx, row in enumerate(grid):
        times_squares_skipped = 0
        for square_idx, square in enumerate(row):
            if square == ".":
                times_squares_skipped += 1
                continue
            if internal_row_idx == 0:
                times_squares_skipped += 1
                continue
        if times_squares_skipped == len(grid[0]):
            rows_skipped += 1
    return rows_skipped


def check_right_diagonal_matches(grid:list[list[str]], external_row_idx: int, piece: str) -> bool:
    skipped_rows = calculate_rows_to_skip(grid)
    chained_piece_count = 1
    chained_position = float("inf")
    for internal_row_idx, row in enumerate(grid[external_row_idx:]):
        print("current row:", row)
        for square_idx, square in enumerate(row):
            if square == "." or square != piece:
                continue
            if internal_row_idx == 0:
                continue
            if square_idx == chained_position+1 and square != piece:
                print(square_idx, chained_position+1, piece)
                chained_piece_count = 1
                continue
            if square == grid[internal_row_idx+skipped_rows-1][square_idx-1]:
                print("----CHAINED PIECE----")
                chained_piece_count += 1
                print(f"piece = {square}, idx = {square_idx}, chained pieces = {chained_piece_count}\n")
                chained_position = square_idx
                if chained_piece_count == 4:
                    return True
                break
            if square_idx != chained_position+1:
                print(f"{square_idx} != {chained_position+1}")
                continue

    return False

#print(check_right_diagonal_matches(grid, 3, "X"))

def check_diagonal_win(grid: list[list[str]]) -> bool:
    for row_idx, row in enumerate(grid):
        print("---")
        print(row)
        print("---")
        for square_idx, square in enumerate(row):
            if square == ".":
                continue
            is_won = check_right_diagonal_matches(grid, row_idx, square)
            if is_won:
                return True
    return False


print(check_diagonal_win(grid))

#def play_game():
#    os.system("clear")
#    draw_grid(grid)
#    while True:
#        for player_number, piece in enumerate(PIECES):
#            print(f"Player {player_number}'s turn: ({piece})")
#            player_turn(grid, piece)
#            os.system("clear")
#            draw_grid(grid)
#            horizontal_or_vertical_win = check_win(grid)
#            diagonal_win = check_diagonal_win(grid)
#            print(horizontal_or_vertical_win, diagonal_win)
#
#
#if __name__ == "__main__":
#    play_game()
#
