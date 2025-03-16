import pytest
from main import check_win, check_diagonal_win_from_left_side, check_diagonal_win_from_right_side

def test_win_horizontally():
    assert check_win([["X","X","X","X",".","."],
                      [".",".",".",".",".","."], 
                      [".",".",".",".",".","."], 
                      [".",".",".",".",".","."],
                      [".",".",".",".",".","."],
                      [".",".",".",".",".","."],
                      [".",".",".",".",".","."]]) == True 

def test_lose_horizontally():
    assert check_win([["X","X",".","X",".","."],
                      [".",".",".",".",".","."], 
                      [".",".",".",".",".","."], 
                      [".",".",".",".",".","."],
                      [".",".",".",".",".","."],
                      [".",".",".",".",".","."],
                      [".",".",".",".",".","."]]) == False 

def test_win_vertically():
    assert check_win([["X",".",".",".",".","."],
                      ["X",".",".",".",".","."], 
                      ["X",".",".",".",".","."], 
                      ["X",".",".",".",".","."],
                      [".",".",".",".",".","."],
                      [".",".",".",".",".","."],
                      [".",".",".",".",".","."]]) == True 

def test_lose_vertically():
    assert check_win([["X",".",".",".",".","."],
                      ["X",".",".",".",".","."], 
                      [".",".",".",".",".","."], 
                      ["X",".",".",".",".","."],
                      [".",".",".",".",".","."],
                      [".",".",".",".",".","."],
                      [".",".",".",".",".","."]]) == False 

def test_win_diagonally_from_left_side():
    assert check_diagonal_win_from_left_side([["O",".",".",".",".","."],
                                              [".","O",".",".",".","."], 
                                              [".",".","O",".",".","."], 
                                              [".",".",".","O",".","."],
                                              [".",".",".",".",".","."],
                                              [".",".",".",".",".","."],
                                              [".",".",".",".",".","."]]) == True

def test_lose_diagonally_from_left_side():
    assert check_diagonal_win_from_left_side([["O",".",".",".",".","."],
                                              [".",".",".",".",".","."], 
                                              [".",".","O",".",".","."], 
                                              [".",".",".","O",".","."],
                                              [".",".",".",".",".","."],
                                              [".",".",".",".",".","."],
                                              [".",".",".",".",".","."]]) == False

def test_win_diagonally_from_right_side():
    assert check_diagonal_win_from_right_side([[".",".",".",".",".","."],
                                               [".",".",".",".",".","."], 
                                               [".",".",".",".",".","."], 
                                               [".",".",".",".",".","O"],
                                               [".",".",".",".","O","."],
                                               [".",".",".","O",".","."],
                                               [".",".","O",".",".","."]]) == True

def test_lose_diagonally_from_right_side():
    assert check_diagonal_win_from_right_side([[".",".",".",".",".","."],
                                               [".",".",".",".",".","."], 
                                               [".",".",".",".",".","."], 
                                               [".",".",".",".",".","O"],
                                               [".",".",".",".","O","."],
                                               [".",".",".",".",".","."],
                                               [".",".","O",".",".","."]]) == False


if __name__ == "__main__":
    main.pytest()
