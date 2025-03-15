"""
get length of word
iterate through the word in the range(half the word)
store each letter in a list
loop through the word but backwards and see if the letters match
"""

def is_palindrome(word: str) -> bool:
    first_half = []
    second_half = []
    length_of_word = len(word)
    for number in range(length_of_word//2):
        first_half.append(word[number])

    for number in range(length_of_word-1, (length_of_word-1)//2, -1):
        second_half.append(word[number])

    if first_half == second_half:
        return True
    
    return False


def main():
    pass
if __name__ == "__main__":
    main()

