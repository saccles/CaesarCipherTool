from string import ascii_lowercase

VALID_CHARS = [letter for letter in ascii_lowercase]

def encrypt(plaintext, key=3):
    """A function that encrypts a string using the Caesar cipher."""
    ciphertext = ""
    for char in plaintext:
        if char.lower() in VALID_CHARS:
            # Get position of character.
            index = VALID_CHARS.index(char.lower())
            # Perform encryption operations.
            new_index = (index + key) % 26
            new_char = VALID_CHARS[new_index]
            if char.isupper():
                new_char = new_char.upper()
        else:
            new_char = char
        ciphertext += new_char
    return ciphertext

def decrypt(ciphertext, key=3):
    """A function that decrypts a string using the Caesar cipher."""
    plaintext = ""
    for char in ciphertext:
        if char.lower() in VALID_CHARS:
            # Get position of character.
            index = VALID_CHARS.index(char.lower())
            # Perform decryption operations. 
            new_index = (index - key) % 26
            new_char = VALID_CHARS[new_index]
            if char.isupper():
                new_char = new_char.upper()
        else:
            new_char = char
        plaintext += new_char
    return plaintext
