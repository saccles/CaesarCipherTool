from time import sleep


def animate(text, time=0.10, colors=None):
    """
    Add basic animation to inputted text in the form of a slight delay
    between the printing of each character in the text.
    """
    for char in text:
        print(char, end="", flush=True)
        sleep(time)
    print()
