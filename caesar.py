# Silas Accles
# 1/31/2024
# Casesar Cipher Tool
# A program that encrypts and decrypts user-input using the Caesar cipher.
# Modified 3/9/2024

from string import ascii_lowercase
from caesar_cipher_functions import encrypt, decrypt
from basic_animation_functions import animate

def raise_error():
    """A simple function for raising user-input error messages."""
    print("Sorry! That is not a valid option.")
    print("Valid Options: 'e' to encrypt, 'd' to decrypt, 'q' to quit.")

# User Input and Choice
program_active = True

# Keep running the loop until program_active is False.
while program_active:
    animate("\n/\---Caesar Cipher Tool---/\\")
    animate("Encrypt or Decrypt?")
    user_choice = input("('e' = encrypt, 'd' = decrypt, 'q' = quit): ")
    
    # Encrypt text.
    if user_choice.lower() == 'e':
        plaintext = input("Enter the text or message to encrypt: ")
        print()
        # Call encryption function.
        ciphertext = encrypt(plaintext)
        animate(f"Input: {plaintext}", time=0.15)
        animate(f"Ciphertext: {ciphertext}", time=0.15)

    # Decrypt text.
    elif user_choice.lower() == 'd':
        ciphertext = input("Enter the text or message to decrypt: ")
        print()       
        # Call decryption function.
        plaintext = decrypt(ciphertext)
        animate(f"Input: {ciphertext}", time=0.15)
        animate(f"Plaintext: {plaintext}", time=0.15)
 
    # Quit program. 
    elif user_choice.lower() == 'q':
        print("\nQuitting!")
        program_active = False

    # Raise an error if an invalid option is chosen. 
    else:
        raise_error()
    


