from caesar_cipher_functions import encrypt, decrypt
from basic_animation_functions import animate, sleep

secret_msg = encrypt("Thanks for listening. Bye for now!")
animate(secret_msg)
print()

sleep(390)

animate(decrypt(secret_msg))

