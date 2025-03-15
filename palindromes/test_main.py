import pytest
from main import is_palindrome

def test_is_palindrome():
    assert is_palindrome("ahha") == True
    assert is_palindrome("ahhhha") == True
    assert is_palindrome("camel") == False
    assert is_palindrome("aha") == True

if __name__ == "__main__":
    main.pytest()