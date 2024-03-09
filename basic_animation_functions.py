from time import sleep

def animate_text(text, time=0.10):
    """A simple function that adds basic animation to an inputted text."""
    for char in text:
        print(char, end="", flush=True)
        sleep(time)
    print()