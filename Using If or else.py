# Using If or else

import time

def start_adventure():
    """Starts the adventure game."""

    print("Welcome to the Game!")
    time.sleep(3)
    print("You find yourself lost floating in the dark. Upon in horizon you find two paths.")
    time.sleep(5)
    print("You choose either Light or Dark.")
    time.sleep(2)

    choice = input("Which way do you choose? (Light/Dark): ").upper()

    if choice == "Light":
        light_path()
    elif choice == "Dark":
        dark_path()
    else:
        print("Invalid choice. Please try again.")
        start_adventure()

def light_path():
    """Handles the light path in the adventure."""

    print("You follow the path of light.")
    time.sleep(1)
    print("You come out of the mouth of a cave. Streched out in front of you is a snow capped mountain range.")
    time.sleep(4)
    print("Down leads to a raging river of ice, Up leads to the peak of the mountain where something glimmers in the sun?")

    choice = input("What do you do? (Down/Up): ").upper()

    if choice == "Down":
        print("You make you way down listening to the rush of water. You find a book laying upon a stump near the water.")
        time.sleep(2)
        print("Welcome your story is only just starting!")
    elif choice == "Up":
        print("You make your way up the mountain, upon reching the summit you find a chest.")
        time.sleep(2)
        print("Opening the chest you find a note. 'Welcome your story is only just starting'")
    else:
        print("Invalid choice. Please try again.")
        light_path()

def dark_path():
    """Handles the dark path in the adventure."""

    print("You follow the path of darkness.")
    time.sleep(2)
    print("You exit upon a dark ans vast forest. The foliage is high above your head and so lush that it blocks nearly all the light.")
    time.sleep(4)
    print("The Right path leads down the denser, darker part of the forest. The Left path leads to a thinning, lighter portion of the forest.")

    choice = input("Where do you go? (Right/Left): ").upper()

    if choice == "Right":
        print("You bravely walk down the darken path. In your thoughts you know.")
        time.sleep(2)
        print("Your story is just starting.")
    elif choice == "Left":
        print("You walk into the growing light of the thinning forest. In your thought you know.")
        time.sleep(2)
        print("Your story is just staring.")
    else:
        print("Invalid choice. Please try again.")
        dark_path()

if __name__ == "__main__":
    start_adventure()
