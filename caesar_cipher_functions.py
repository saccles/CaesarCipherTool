from string import ascii_lowercase

VALID_CHARS = [letter for letter in ascii_lowercase]
KEY = 3

def encrypt(plaintext):
    """A function that encrypts a string using the Caesar cipher."""
    ciphertext = ""
    for char in plaintext:
        if char.lower() in VALID_CHARS:
            # Get position of character.
            index = VALID_CHARS.index(char.lower())
            # Perform encryption operations.
            new_index = (index + KEY) % 26
            new_char = VALID_CHARS[new_index]
            if char.isupper():
                new_char = new_char.upper()
        else:
            new_char = char
        ciphertext += new_char
    return ciphertext

def decrypt(ciphertext):
    """A function that decrypts a string using the Caesar cipher."""
    plaintext = ""
    for char in ciphertext:
        if char.lower() in VALID_CHARS:
            # Get position of character.
            index = VALID_CHARS.index(char.lower())
            # Perform decryption operations. 
            new_index = (index - KEY) % 26
            new_char = VALID_CHARS[new_index]
            if char.isupper():
                new_char = new_char.upper()
        else:
            new_char = char
        plaintext += new_char
    return plaintext
