from string import ascii_lowercase
from time import sleep

VALID_CHARS = [letter for letter in ascii_lowercase]
KEY = -3

def encode_text(plaintext):
    """A function that encodes a string using the caesar cipher."""
    ciphertext = ""
    for char in plaintext:
        if char.lower() in VALID_CHARS:
            # Get position of character.
            index = VALID_CHARS.index(char.lower())
            # Perform encoding operations.
            new_index = (index + KEY) % 26
            new_char = VALID_CHARS[new_index]
            if char.isupper():
                new_char = new_char.upper()
        else:
            new_char = char
        ciphertext += new_char
    return ciphertext

def decode_text(ciphertext):
    """A function that decodes a string using the caesar cipher."""
    plaintext = ""
    for char in ciphertext:
        if char.lower() in VALID_CHARS:
            # Get position of character.
            index = VALID_CHARS.index(char.lower())
            # Perform decoding operations. 
            new_index = (index - KEY) % 26
            new_char = VALID_CHARS[new_index]
            if char.isupper():
                new_char = new_char.upper()
        else:
            new_char = char
        plaintext += new_char
    return plaintext
