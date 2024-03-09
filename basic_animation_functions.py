from time import sleep

def animate(text, time=0.10, colors=None):
    """A simple function that adds basic animation to an inputted text."""
    for char in text:
        print(char, end="", flush=True)
        sleep(time)
    print()
