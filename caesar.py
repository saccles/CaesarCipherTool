# Silas Accles
# 1/31/2024
# Casesar Cipher ENCODER/DECODER
# A program that encodes and decodes simple user input using the caesar cipher.

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

def animate_text(text, time=0.10):
    """A simple function that adds basic animation to an inputted text."""
    for char in text:
        print(char, end="", flush=True)
        sleep(time)
    print()

# User Input and Choice
program_active = True

# Keep running the loop until program_active is False.
while program_active:
    animate_text("\n/\---Caesar Cipher ENCODER/DECODER---/\\")
    animate_text("Encode or Decode?")
    user_choice = input("('e' for encode, 'd' for decode, 'q' for quit): ")
    
    # Encode text.
    if user_choice.lower() == 'e':
        plaintext = input("Enter the text or message you wish to encode\n: ")
        # Call encoding function.
        ciphertext = encode_text(plaintext)
        animate_text(f"Input: {plaintext}", time=0.15)
        animate_text(f"Ciphertext: {ciphertext}", time=0.15)

    # Decode text.
    elif user_choice.lower() == 'd':
        ciphertext = input("Enter the text or message you wish to decode\n: ")
        # Call decoding function.
        plaintext = decode_text(ciphertext)
        animate_text(f"Input: {ciphertext}", time=0.15)
        animate_text(f"Plaintext: {plaintext}", time=0.15)
 
    # Quit program. 
    elif user_choice.lower() == 'q':
        animate_text("\nQuitting Program!")
        program_active = False

    else:
        print("Sorry! That is not a valid option.")


