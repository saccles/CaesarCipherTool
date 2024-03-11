from caesar_cipher_functions import encrypt, decrypt
from basic_animation_functions import animate, sleep

secret_msg = encrypt("Thanks for listening. Bye for now!")
animate(f"\n{secret_msg}")
print()


