import random
import time
from art import start_logo, end_logo

# Global variables & data structure
game_round = 0
continue_play = True
user_response = ""
ship_list = []

def  welcome_screen():
    print(start_logo)
    print("\n Welcome to Star Trek Attack Wing (STAW): Solitaire \n\n")

def game_setup():
    ship_count = 0

    print(" Game Setup\n")
    print(" ==========\n")
    ship_count = int(input(" How many ships are you going to play: "))

    if ship_count <= 1:
        print("\n Sorry, the game requires at least two (2) ships to play.")
    else:
        print(f"\n Please enter individual names of the {ship_count} ships.")

        for ship in range(0, ship_count):
            ship_name = str(input(f" >> Ship Name {ship + 1}: "))
            ship_list.append(ship_name)

    print(f"\n Names of {ship_count} ships have been collected.")
    print("\n Commencing STAW: Solitaire in 3 seconds.. ")
    time.sleep(3)

def clear_terminal_screen():
    print("\n" * 100)

def generate_ship_list(action):
    for ship in range(0, len(ship_list)):
        print(f" Ship to {action} #{ship + 1}: {ship_list[ship]}")

def activation_phase():
    clear_terminal_screen()
    print(f" Activation Phase Round # {game_round + 1}")
    print(" ============================ ")

    random.shuffle(ship_list)
    generate_ship_list("move")
    print("\n NOTE: Implement corresponding Action after moving each ship.")

def combat_phase():
    clear_terminal_screen()
    print(f" Combat Phase Round # {game_round + 1}")
    print("\n ======================== ")
    random.shuffle(ship_list)
    generate_ship_list("attack")

def end_phase():
    clear_terminal_screen()
    print(f" End Phase Round # {game_round + 1}")
    print("\n ===================== ")
    print(''' 1.) Flip back disabled (not destroyed) Shield tokens to their active states.\n\n 2.) Remove all remaining BattleStation, Evade, Scan and Red Cloak tokens.\n\n 3.) Retain all Target Lock tokens.\n\n 4.) Green Cloak tokens may be retained (player discretion).

    ''')

# Terminate program
def terminate_program():
    clear_terminal_screen()
    print(end_logo)
    print(''' Thank you for playing Star Trek Attack Wing (STAW): Solitaire
    ''')

welcome_screen()
game_setup()

while continue_play:
    activation_phase()
    print("\n Moving to -= Combat Phase =-")
    proceed_to_combat = input("\n Press [y] to proceed: ").lower()

    if proceed_to_combat == 'y':
        combat_phase()

    print("\n Moving to -= End Phase =-")
    proceed_to_end = input("\n Press [y] to proceed: ").lower()

    if proceed_to_end == 'y':
        end_phase()

    print("\n Commencing next round...")
    next_round = input("\n Press [y] to proceed, any key to terminate: ").lower()

    if next_round == 'y':
        game_round += 1
    else:
        continue_play = False
        terminate_program()
