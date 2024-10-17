import time
import random

# Player inventory and health variables
inventory = []

def start_adventure():
    """Starts the adventure game."""
    global player_name

    print("Welcome to the Game!")
    time.sleep(2)
    player_name = input("Enter your character's name: ")
    print(f"Hello, {player_name}! Your adventure begins now.")
    time.sleep(2)
    print("You find yourself lost, floating in the dark. Upon the horizon, you see two paths.")
    time.sleep(3)
    print("You must choose: the Light path or the Dark path.")
    time.sleep(2)

    choice = input("Which way do you choose? (Light/Dark): ").upper()

    if choice == "LIGHT":
        Light_path()
    elif choice == "DARK":
        Dark_path()
    else:
        print("Invalid choice. Please try again.")
        start_adventure()

# Inventory handling
def add_to_inventory(item):
    inventory.append(item)
    print(f"You have picked up: {item}")
    time.sleep(1)

def use_item(item):
    if item in inventory:
        print(f"You used: {item}")
        # Random chance to break item when used
        if random.choice([True, False]):
            print(f"But your {item} breaks after use!")
            inventory.remove(item)
        else:
            print(f"You keep your {item} after using it.")
    else:
        print(f"You don't have a {item}.")
    time.sleep(1)

def show_inventory():
    if inventory:
        print(f"Your inventory: {', '.join(inventory)}")
    else:
        print("Your inventory is empty.")
    time.sleep(1)

# Light Path with Events
def Light_path():
    """Handles the light path in the adventure."""
    print("You follow the path of light.")
    time.sleep(1)
    print("You come out of the mouth of a cave. Stretched out in front of you is a snow-capped mountain range.")
    time.sleep(4)
    print("Down leads to a raging river of ice, Up leads to the peak of the mountain where something glimmers in the sun.")
    choice = input("What do you do? (Down/Up): ").upper()

    if choice == "DOWN":
        light_river_path()
    elif choice == "UP":
        light_mountain_path()
    else:
        print("Invalid choice. Please try again.")
        Light_path()

def light_river_path():
    """Down the river path, leading to an item event and a major challenge."""
    print("You make your way down, listening to the rush of water. The icy river sends chills down your spine.")
    time.sleep(2)
    print("As you walk, you spot something shiny partially buried in the snow.")
    time.sleep(2)
    choice = input("Do you investigate the shiny object? (Yes/No): ").upper()

    if choice == "YES":
        print("You dig it out and find a glistening dagger!")
        add_to_inventory("Dagger")
        print("The blade feels cold in your hand, and it might serve you well.")
    else:
        print("You decide to leave the object behind and continue your journey.")

    time.sleep(2)
    print("Suddenly, you hear a loud rumble, and a crack splits the ice nearby!")
    time.sleep(2)
    print("A massive ice troll appears, blocking your path!")

    if "Dagger" in inventory:
        print("You can choose to fight the troll with your dagger.")
        choice = input("Do you fight the troll? (Yes/No): ").upper()
        if choice == "YES":
            print("You bravely charge at the troll, slashing with your dagger!")
            time.sleep(2)
            print("After a fierce battle, you emerge victorious!")
            time.sleep(2)
        else:
            print("You decide to run, narrowly escaping the troll's grasp but losing the chance to defeat it.")
            time.sleep(2)
            # If the player did not fight, we still let them move on
    else:
        print("You have no weapon to defend yourself. The troll easily overpowers you, ending your journey.")
        time.sleep(2)
        game_over()

    # Add a narrative of traveling after the troll fight
    print("After the battle, you take a moment to catch your breath.")
    time.sleep(2)
    print("You continue your journey, walking for a while through the snowy terrain.")
    time.sleep(2)
    
    # Introduce the puzzle after traveling
    if light_puzzle_after_troll():
        print("You solve the puzzle and receive the Amulet!")
        add_to_inventory("Amulet")
    else:
        print("You couldn't solve the puzzle and move on empty-handed.")

    time.sleep(2)
    # Continue to the final path after the river
    light_final_path()

def light_mountain_path():
    """Up the mountain path, leading to a different item event and major challenge."""
    print("You make your way up the mountain. Upon reaching the summit, you find a chest and a strange lever.")
    time.sleep(2)
    print("A sign reads: 'Only one can be used, choose wisely.'")

    choice = input("Do you open the chest or pull the lever? (Chest/Lever): ").upper()

    if choice == "CHEST":
        print("You open the chest and find a shining amulet.")
        add_to_inventory("Amulet")
        print("You decide to wear it; it pulses with magical energy.")
    elif choice == "LEVER":
        print("You pull the lever, and the ground beneath you opens up!")
        if "Amulet" in inventory:
            print("The amulet glows and creates a protective barrier, saving you from falling.")
        else:
            print("Without protection, you fall into a deep chasm.")
            time.sleep(2)
            game_over()

    time.sleep(2)
    print("After your decision, you hear a roar in the distance. A massive rockslide is heading your way!")
    time.sleep(2)

    if "Amulet" in inventory:
        print("You can choose to use the amulet to shield yourself from the rocks.")
        choice = input("Do you use the amulet? (Yes/No): ").upper()
        if choice == "YES":
            print("You activate the amulet, and a magical barrier surrounds you, protecting you from the falling rocks.")
            print("You emerge unscathed, but the path ahead is now blocked.")
            time.sleep(2)
        else:
            print("You attempt to dodge the rocks, but they crush you!")
            time.sleep(2)
            game_over()
    else:
        print("You have no protection, and the rocks bury you alive.")
        time.sleep(2)
        game_over()

    # Add narrative of traveling after the rockslide event
    print("After the rockslide, you gather your thoughts and carefully navigate around the debris.")
    time.sleep(2)
    print("You walk for some time, reflecting on your journey so far.")
    time.sleep(2)

    # Introduce the puzzle after traveling
    if mountain_puzzle_after_amulet():
        print("You solve the puzzle and receive a Glowing Carrot!")
        add_to_inventory("Glowing Carrot")
    else:
        print("You couldn't solve the puzzle and move on without the carrot.")
    
    light_final_path()

def light_puzzle_after_troll():
    """Puzzle for the Light path after defeating the troll."""
    print("You come across an ancient stone with a riddle:")
    time.sleep(2)
    print("'What has keys but can't open locks?'")
    time.sleep(2)

    choice = input("Solve the riddle: ").lower()

    if choice == "piano":
        return True  
    else:
        return False  

def mountain_puzzle_after_amulet():
    """Puzzle for the mountain path after receiving the Amulet."""
    print("You notice a glowing inscription on the wall:")
    time.sleep(2)
    print("'I can be cracked, made, told, and played. What am I?'")
    time.sleep(2)

    choice = input("Solve the riddle: ").lower()

    if choice == "joke":
        return True  # Puzzle solved correctly
    else:
        return False  # Puzzle failed

def light_final_path():
    """The final part of the light path leading to the story's conclusion."""
    print("After your trials, you reach a safe clearing to rest.")
    time.sleep(2)
    print(f"As {player_name}, you feel a sense of accomplishment. You continue forward.")
    time.sleep(2)
    major_event()

# Handles the Dark Path
def Dark_path():
    """Handles the dark path in the adventure."""
    print("You follow the path of darkness.")
    time.sleep(2)
    print("You exit into a dark and vast forest. The foliage is high above your head, so lush that it blocks nearly all the light.")
    time.sleep(4)
    print("The Right path leads down the denser, darker part of the forest. The Left path leads to a thinning, lighter portion of the forest.")

    choice = input("Where do you go? (Right/Left): ").upper()

    if choice == "RIGHT":
        dark_forest_path()
    elif choice == "LEFT":
        light_forest_path()
    else:
        print("Invalid choice. Please try again.")
        Dark_path()

def dark_forest_path():
    """The dark forest path filled with macabre enemies and item events."""
    print("You brave the dark forest, hearing the scurrying of unseen creatures.")
    time.sleep(2)
    print("Suddenly, you stumble upon a glint of metal in the underbrush.")
    time.sleep(2)
    
    choice = input("Do you investigate the metal object? (Yes/No): ").upper()

    if choice == "YES":
        print("You discover a rusty sword, but you can feel a dark aura around it.")
        add_to_inventory("Rusty Sword")
        print("It may not be the best weapon, but it could serve you in a pinch.")
    else:
        print("You decide to avoid it and continue deeper into the forest.")

    time.sleep(2)
    print("As you proceed, a gigantic spider descends from the trees above!")
    time.sleep(2)

    if "Rusty Sword" in inventory:
        print("You can choose to fight the spider with your rusty sword.")
        choice = input("Do you attack the spider? (Yes/No): ").upper()
        if choice == "YES":
            print("You swing your rusty sword, and after a fierce battle, you defeat the spider!")
            time.sleep(2)
        else:
            print("You attempt to run, but the spider catches you!")
            time.sleep(2)
            game_over()
    else:
        print("You have no weapon to defend yourself, and the spider quickly overpowers you!")
        time.sleep(2)
        game_over()

    # Narrative after spider fight
    print("After the battle, you catch your breath and look around.")
    time.sleep(2)
    print("The forest feels eerie, yet you press on, determined to find your way.")
    time.sleep(2)
    print("Eventually, you come across a stone altar in a small clearing.")
    time.sleep(2)

    # Introduce a puzzle for the Dark path
    dark_puzzle_amulet()

def light_forest_path():
    """A lighter path through the forest, leading to a different item event."""
    print("You venture along the lighter path, where beams of moonlight pierce through the treetops.")
    time.sleep(2)
    print("Suddenly, you find an ancient stone pedestal with an amulet resting on top.")
    time.sleep(2)
    print("A sign warns: 'Only the brave may take what lies here.'")
    
    choice = input("Do you take the amulet? (Yes/No): ").upper()
    
    if choice == "YES":
        print("You reach for the amulet, feeling a surge of power as it melds into your being.")
        add_to_inventory("Amulet")
    else:
        print("You decide not to take the risk and continue your journey.")

    time.sleep(2)
    print("As you proceed, shadows begin to swirl around you, and a dark figure emerges!")
    time.sleep(2)

    if "Amulet" in inventory:
        print("You can choose to use the amulet's power against the dark figure.")
        choice = input("Do you use the amulet? (Yes/No): ").upper()
        if choice == "YES":
            print("You channel the amulet's power and cast a protective barrier around yourself.")
            print("The figure recoils in fear and disappears into the shadows.")
            time.sleep(2)
        else:
            print("You attempt to reason with the dark figure, but it has no interest in talking!")
            time.sleep(2)
            game_over()
    else:
        print("You have no means to defend yourself, and the figure captures you!")
        time.sleep(2)
        game_over()

    # Narrative after dark figure encounter
    print("After the figure vanishes, you take a moment to steady yourself.")
    time.sleep(2)
    print("You wander through the forest, feeling a strange pull towards a flickering light.")
    time.sleep(2)
    print("As you approach, you find an old, moss-covered chest lying among the roots of a tree.")
    time.sleep(2)

    # Introduce a puzzle for the dark figure encounter
    dark_puzzle_dagger()

def dark_final_path():
    """The final part of the dark path leading to the story's conclusion."""
    print("After your encounters, you finally catch your breath.")
    time.sleep(2)
    print(f"As {player_name}, you feel a mixture of dread and excitement. You continue to march forward.")
    time.sleep(2)
    major_event()

def dark_puzzle_amulet():
    """Puzzle for the Dark path after spider fight."""
    print("On the altar, you find a riddle inscribed on the stone:")
    time.sleep(2)
    print("'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?'")
    time.sleep(2)

    choice = input("Solve the riddle: ").lower()

    if choice == "echo":
        print("The altar glows, revealing a hidden compartment containing a mystical amulet!")
        add_to_inventory("Amulet")
        dark_final_path()
    else:
        print("The altar remains silent, and you continue on your journey without the treasure.")
        time.sleep(2)

def dark_puzzle_dagger():
    """Puzzle for the Dark figure encounter."""
    print("The chest creaks open to reveal an ancient scroll with a riddle:")
    time.sleep(2)
    print("'What has keys but can't open locks?'")
    time.sleep(2)

    choice = input("Solve the riddle: ").lower()

    if choice == "piano":
        print("The chest clicks open further, revealing a beautifully crafted dagger inside!")
        add_to_inventory("Dagger")
        dark_final_path()
    else:
        print("The chest closes, and you leave without claiming the dagger.")
        time.sleep(2)
# Major event leading to choice
def major_event():
    """A major heroic event before reaching the city of Darust."""
    print("You find yourself at the edge of a massive cliff, overlooking a dark valley.")
    time.sleep(2)
    print("You hear cries for help and see a figure struggling against a dark creature below.")
    time.sleep(2)
    print("You must decide whether to help or ignore the cries.")

    choice = input("Will you help the figure? (Help/Ignore): ").upper()

    if choice == "HELP":
        print("You bravely climb down the cliff to assist the figure.")
        time.sleep(2)
        print("As you approach, you realize it's a trapped adventurer being attacked by a dark beast!")
        time.sleep(2)

        # Inform the player of their inventory
        print("\nYour current inventory:")
        if len(inventory) > 0:
            for item in inventory:
                print(f"- {item}")
        else:
            print("You have no items in your inventory.")
        print()

        # Ask the player to choose an item or not use one
        choice = input("Which item will you use to help the adventurer? (Rusty Sword/Dagger/Amulet/Glowing Carrot/None): ").upper()

        # Handle each item based on player choice
        if choice == "RUSTY SWORD" and "Rusty Sword" in inventory:
            print("You strike valiantly with your rusty sword!")
            time.sleep(2)
            print("After a fierce battle, you defeat the creature and rescue the adventurer.")
            time.sleep(2)
            print("The adventurer is grateful and offers you a powerful potion as a reward!")
            add_to_inventory("Powerful Potion")

        elif choice == "DAGGER" and "Dagger" in inventory:
            print("You strike bravely with your dagger!")
            time.sleep(2)
            print("After a fierce battle, you defeat the creature and rescue the adventurer.")
            time.sleep(2)
            print("The adventurer is grateful and offers you a powerful potion as a reward!")
            add_to_inventory("Powerful Potion")

        elif choice == "GLOWING CARROT" and "Glowing Carrot" in inventory:
            if len(inventory) == 2 and "Amulet" in inventory:
                print("You throw the glowing carrot, and the creature is mesmerized!")
                time.sleep(2)
                print("You seize the opportunity to rescue the adventurer.")
                inventory.remove("Glowing Carrot")
                print("The adventurer is grateful and offers you both a powerful potion and a magic wand as a reward!")
                add_to_inventory("Powerful Potion")
                add_to_inventory("Magic Wand")
            else:
                print("You throw the glowing carrot, and the creature is mesmerized!")
                time.sleep(2)
                print("You seize the opportunity to rescue the adventurer.")
                inventory.remove("Glowing Carrot")
                print("The adventurer is grateful and offers you a powerful potion as a reward!")
                add_to_inventory("Powerful Potion")

        elif choice == "AMULET" and "Amulet" in inventory:
            print("You channel the amulet's energy, creating a protective shield around you.")
            time.sleep(2)
            print("The creature attacks relentlessly, but your shield holds strong.")
            time.sleep(2)
            print("Eventually, the dark beast gives up, realizing it cannot break through your defenses.")
            time.sleep(2)
            print("The adventurer is amazed and grateful for your bravery.")
            add_to_inventory("Powerful Potion")
            print("The adventurer offers you a powerful potion as a reward!")

        elif choice == "NONE":
            # The player loses all items in this scenario
            print("You choose not to use any item.")
            time.sleep(2)
            print("Without any means to defend yourself, the creature attacks. Though you manage to fend it off, you lose all of your possessions in the struggle!")
            time.sleep(2)
            inventory.clear()  # Clear all items from inventory
            print("You have lost all of your items!")
            time.sleep(2)
            print("With no rewards or items left, you press on toward the city, weary but determined.")

        else:
            print("You hesitate or choose an item you don't possess, and the creature overpowers you both!")
            time.sleep(2)
            game_over()

    else:
        print("You ignore the cries and continue on your way.")
        time.sleep(2)
        print("You feel a pang of guilt but decide to push on.")
        time.sleep(2)

    # Narrative after the major event
    print("After this harrowing experience, you continue your journey towards the city.")
    time.sleep(2)
    print("The path is long and filled with challenges, but your heart is filled with determination.")
    time.sleep(2)

    # Proceed to the castle city
    castle_city_intro()
# The City of Darust
def castle_city_intro():
    """Introduce the Castle City of Darust."""
    print("You arrive at the gates of the city, it is a magical city bustling with life.")
    time.sleep(2)
    print("The grand castle towers over everything, its spires touching the sky, shimmering with a light that seems almost otherworldly.")
    time.sleep(3)
    print("The air is filled with the scent of exotic spices and the sounds of laughter and chatter.")
    time.sleep(2)
    castle_city_adventure()

def castle_city_adventure():
    """Choose where to explore in the castle city."""
    print("You stand in the heart of the city, and you have several options to explore:")
    print("1. The Market District")
    print("2. The Viewpoint to see the Castle")
    print("3. Head straight to the Adventurer's Hall")

    choice = input("Where would you like to go? (1/2/3): ").upper()

    if choice == "1":
        market_district()
    elif choice == "2":
        castle_viewpoint()
    elif choice == "3":
        adventurers_hall()
    else:
        print("Invalid choice. Please try again.")
        castle_city_adventure()

def market_district():
    """Visit the Market District."""
    print("You walk through the bustling market, filled with vendors selling magical artifacts, exotic foods, and strange potions.")
    time.sleep(2)
    print("You see creatures of all kinds: dwarves, elves, humans, and even more mysterious beings.")
    time.sleep(2)
    print("After some time exploring, you decide it's time to move on.")
    time.sleep(2)
    castle_city_adventure()

def castle_viewpoint():
    """See the grand castle from the viewpoint."""
    print("You make your way to a high viewpoint, where you can see the entire city below.")
    time.sleep(2)
    print("The grand castle towers over everything, its magical aura glowing brighter the closer you get.")
    time.sleep(2)
    print(f"{player_name}, you feel a sense of awe and destiny pulling you toward the castle.")
    time.sleep(2)
    castle_city_adventure()

def adventurers_hall():
    """Enter the Adventurer's Hall and conclude the current adventure."""
    print("You arrive at the Adventurer's Hall, a massive building adorned with banners and flags from all corners of this world.")
    time.sleep(2)
    print("Inside, you see adventurers of all kinds: elves, dwarves, humans, orcs, and even more exotic beings.")
    time.sleep(3)
    print("Weapons clang, stories are shared, and a magical warmth fills the air.")
    time.sleep(3)
    print("As you approach the front desk, a beautiful elven woman greets you.")
    time.sleep(2)
    print(f"'Welcome to Darust, {player_name}. How can the Adventure Society help you?'")
    time.sleep(3)
    print("Till the next installment.")
    time.sleep(2)

def game_over():
    """Game over message."""
    print("Your adventure ends here. Better luck next time!")
    time.sleep(2)
    exit()

# Start the game
start_adventure()


