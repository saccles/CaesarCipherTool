from time import sleep


def animate(text, time=0.10):
    """
    Add basic animation to inputted text in the form of a slight delay
    between the printing of each character in the text.
    
    Arguments:
        text (str): the text to animate
        time (float, keyword): the delay between animating each character (default 0.10 seconds)
    """
    for char in text:
        print(char, end="", flush=True)
        sleep(time)
    print()
