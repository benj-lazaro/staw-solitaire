import random
import time
from art import start_logo, end_logo

def clear_terminal_screen():
    """Clears the terminal screen."""
    print("\n" * 100)

def welcome_screen():
    """Display the game's welcome screen."""
    clear_terminal_screen()
    print(start_logo)
    print("\n Welcome to Star Trek Attack Wing (STAW): Solitaire \n\n")

def randomize_ship_items(ship_list):
    """Takes a ship list, randomize order of items & returns an updated list."""
    return random.shuffle(ship_list)

def generate_ship_list(ship_list, game_phase):
    """Takes a ship list, print items and corresponding game phase"""
    for ship in range(len(ship_list)):
        print(f" Ship to {game_phase} # {ship + 1}: {ship_list[ship]}\n")

def activation_phase(ship_list, game_round):
    """Takes a ship list, game round & determines the movement order of each ship."""
    clear_terminal_screen()
    print(f" Activation Phase Round # {game_round + 1}")
    print(" =========================== ")
    randomize_ship_items(ship_list)
    generate_ship_list(ship_list, "Move")
    print("\n NOTE: Implement corresponding Action after each ship has moved.")
    return ship_list

def combat_phase(ship_list, game_round):
    """Takes a ship list, game round & determines the attack order of each ship."""
    clear_terminal_screen()
    print(f" Combat Phase Round # {game_round + 1}")
    print(" ======================= ")
    randomize_ship_items(ship_list)
    generate_ship_list(ship_list, "Attack")
    print("\n NOTE: Implement corresponding Action after each ship has moved.")
    return ship_list

def end_phase(game_round):
    """Displays the clean up rules on terminal."""
    clear_terminal_screen()
    print(f" End Phase Round # {game_round + 1}")
    print(" ==================== ")
    print(''' 1.) Flip back disabled (not destroyed) Shield tokens to their active states.\n\n 2.) Remove all remaining BattleStation, Evade, Scan and Red Cloak tokens.\n\n 3.) Retain all Target Lock tokens.\n\n 4.) Green Cloak tokens may be retained (player discretion).

    ''')

def end_screen():
    """Display the game's ending screen."""
    print(end_logo)
    print("\n Thank you for playing Star Trek Attack Wing (STAW): Solitaire \n\n")

# Main Program
game_round = 0
ships_to_play = 0
is_game_over = False
ship_list = []

welcome_screen()
ships_to_play = int(input(" How many ships to play: "))

# Game Setup
if ships_to_play < 2:
    clear_terminal_screen()
    print("\n Opps! Sorry the game requires at least two (2) ships to play.\n\n")
    end_screen()
else:
    print(f"\n Please enter individual names of the {ships_to_play} ships.")

    for ship in range(ships_to_play):
        ship_name = str(input(f" >> Ship Name {ship + 1}: "))
        ship_list.append(ship_name)

    print(f"\n Thank you; the names of {ships_to_play} ships have been collected.")
    print("\n Commencing -= Activation Phase =- in 3 seconds.. ")
    time.sleep(3)

# Star Game
while not is_game_over:
    # Activation Phase
    activation_phase(ship_list, game_round)

    print("\n Proceeding to -= Combat Phase =-")
    next_phase = str(input(" Press 'y' to proceed, 'n' to terminate: "))

    if next_phase == 'n':
        is_game_over = True
    else:
        # Combat Phase
        combat_phase(ship_list, game_round)
        print("\n Proceeding to -= End Phase =-")
        next_phase = str(input(" Press 'y' to proceed, 'n' to terminate: "))

        if next_phase == 'n':
            is_game_over = True
        else:
            # End Phase
            end_phase(game_round)
            print("\n Proceeding to next game round...")
            next_phase = str(input(" Press 'y' to proceed, 'n' to terminate: "))

            if next_phase == 'n':
                is_game_over = True
            else:
                # Next Game Round
                game_round += 1

# End Game
clear_terminal_screen()
end_screen()
