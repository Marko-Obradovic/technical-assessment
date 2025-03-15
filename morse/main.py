"""

"""
char_mapping = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
'--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
'--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
'...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
'-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
'....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
'----.': '9', '-----': '0'}

def translate_morse_letter_to_english_letter(morse: str) -> str:
    if char_mapping[morse] not in char_mapping.values():
        raise KeyError()
    return char_mapping[morse]


def separate_morse_characters(morse: str) -> list[str]:
    return morse.split(" ")


def generate_english_word(morse: list[str]) -> str:
    pass
