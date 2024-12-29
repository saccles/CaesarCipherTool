from string import ascii_lowercase

VALID_CHARS = [letter for letter in ascii_lowercase]


def encrypt(plaintext, key=3):
    """
    Encrypt a plaintext string using the Caesar cipher 
    and return a ciphertext string.

    Arguments:
        plaintext (str): the message or text to encrypt
        key (int, keyword): the encryption key (default 3)

    Returns:
        ciphertext (str): the ciphertext corresponding to the plaintext
    """
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
    """
    Decrypt a ciphertext string using the Caesar cipher 
    and return a plaintext string.

    Arguments:
        ciphertext (str): the message or text to decrypt
        key (int, keyword): the decryption key (default 3)

    Returns:
        plaintext (str): the plaintext corresponding to the ciphertext
    """
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
