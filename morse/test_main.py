import pytest
from main import translate_morse_letter_to_english_letter, separate_morse_characters, generate_english_word

def test_translate_morse_to_english():
    assert translate_morse_letter_to_english_letter(".-") == "A"
    assert translate_morse_letter_to_english_letter("....-") == "4"


def test_translate_morse_to_english_gives_error_with_invalid_morse():
    with pytest.raises(KeyError):
        assert translate_morse_letter_to_english_letter("............-")


def test_separate_morse_characters():
    assert separate_morse_characters(".- -... -.-.") == [".-", "-...", "-.-."]



if __name__ == "__main__":
    main.pytest()