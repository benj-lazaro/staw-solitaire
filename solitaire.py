# Import module
import random

# Global variables
current_round = 0
end_round = 0
number_of_ships = 0

# Global data structure
ship_list = []

# Get ship names from user
def get_ship_names():
    print("LCARS>> Please provide the name of individual ships:\n")

    for ship in range(0, number_of_ships):
        ship_name = str(input(f"  Ship Name {ship + 1}: ")).lower()
        ship_list.append(ship_name)

    print("\n")

# Generate ship list
def generate_ship_list():
    for ship in range(0, len(ship_list)):
        print(f"  Ship {ship + 1}: {ship_list[ship]}")

# Activation Phase
def activation_phase():
    print(f"LCARS>> ACTIVATION PHASE Round # {current_round + 1}\n")

    # Mimic variant chit-pull mechanism; shuffle list items
    random.shuffle(ship_list)

    # List the order of ship movement (i.e. who goes first)
    generate_ship_list()
    print("\n")

# Combat Phase
def combat_phase():
    print(f"LCARS>> COMBAT PHASE Round # {current_round + 1}\n")

    # Mimic variant chit-pull mechanism; shuffle list items
    random.shuffle(ship_list)

    # List the order of ship attack (i.e. who fires first)
    generate_ship_list()
    print("\n")

# End Phase
def end_phase():
    # Display 'clean up' rules
    print(f"LCARS>> END PHASE Round # {current_round + 1}\n")
    print("LCARS>> Flip back disabled Shield Tokens to their active states.\n")
    print("        Remove all remaining BatteStation, Evade, Scan & Red Cloak Tokens.\n")
    print("        Retain all Target Lock Tokens.\n")
    print("        Green Cloak Tokens may be retained (player discretion).\n")

# Terminate program
def end_program():
    # Display message before terminating the program
    print("LCARS>> Thank you for playing Star Trek Attack Wing: Solitaire.\n")
    print("LCARS>> End program.\n")
    exit()

# Display greeting
print("\n--[ Star Trek Attack Wing: Solitaire ]--\n\n")

# Game setup
number_of_ships = int(input("LCARS>> How many ships will you be playing today: "))

if (number_of_ships <= 1):
    print("\nLCARS>> Error! At least two (2) ships are required in order to play.\n")
    end_program()
else:
    print(f"\nLCARS>> Noted. You will be playing a total of {number_of_ships} ships.\n")
    print("*************************************************************************\n")
    get_ship_names()
    print("LCARS>> Ship names have been collected. Beggining solitaire gameplay.\n")
    print("*********************************************************************\n")

# Solitaire gameplay
while (end_round != 1):
    activation_phase()
    any_key = input("LCARS>> Press ENTER to move into COMBAT PHASE\n\n")

    combat_phase()
    any_key = input("LCARS>> Press ENTER to move into END PHASE\n\n")

    end_phase()

    # Increment round counter by 1
    current_round += 1

    # Display option to continue game or terminate program
    user_response = str(input("LCARS>> Press [y] to end round (game) or press ENTER to continue: ")).lower()

    if (user_response == 'y'):
        print("\n")
        end_program()
    else:
        print("********************************************************\n")
