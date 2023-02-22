from random import shuffle

game_round = 1
ship_list = []
is_game_on = True


def welcome_screen():
    """welcome_screen() returns a welcome screen."""
    print("Welcome to Star Trek Attack Wing: Solitaire Gameplay")


def end_screen():
    """end_screen() returns a thank-you message."""
    print("Thank you for playing Star Trek Attack Wing: Solitaire")


def get_ship_name(ship_count, list_data):
    """get_ship_name(int, list) accepts user input and append as items to the list."""
    for ship in range(ship_count):
        ship_name = str(input("Enter name of ship: "))
        list_data.append(ship_name)


def shuffle_ships(list_data):
    """shuffle_ships(list) returns a randomized list items."""
    return shuffle(list_data)


def generate_ship_list(list_data, game_phase):
    """generate_ship_list(list, str) displays list of ships based on current game phase."""
    print(f"List of ships to {game_phase} in succession.")
    for ship in range(len(list_data)):
        print(f"{ship}: {list_data[ship]}")


def ship_destroyed(list_data, index_value):
    """ship_destroyed(list) removes destroyed ship(s) from the list."""
    return list_data.pop(index_value)


def movement_phase(list_data, game_rnd):
    """movement_phase(list, int) returns a list of ships to move in succession."""
    shuffle_ships(list_data)
    print(f"\nMovement Phase Round {game_rnd}")
    return generate_ship_list(list_data, "move")


def attack_phase(list_data, game_rnd):
    """attack_phase(list, int) returns a list of ship to attack in succession."""
    ship_down = True
    shuffle_ships(list_data)
    print(f"\nAttack Phase Round {game_rnd}")
    generate_ship_list(list_data, "attack")

    user_response = str(input("\nAre there any ships destroyed [y/n]? ")).lower()

    if user_response == 'y':
        while ship_down:
            print("Enter the destroyed ship's index number or x to exit:")
            ship_index = input("Ship Index Number: ")

            if ship_index == "x":
                ship_down = False
            else:
                ship_destroyed(list_data, int(ship_index))
                generate_ship_list(list_data, "attack")


def end_phase(game_rnd):
    """end_phase(int) returns multi-line text on end / clean-up phase of the game."""
    print(f"\nEnd Phase Round {game_rnd}")
    print("----")
    print("1.) Flip back disabled Shield token(s) to their active sides for free.")
    print("2.) Remove all remaining Scan, Evade, Battle stations & red Cloak tokens.")
    print("3.) Ships with green Clock tokens can choose to keep their Shield tokens disabled & remain cloaked.")
    print("4.) Retain all Target Lock tokens.")
    print("----")


def declare_victor(ship):
    """declare_victor(list) returns the name of the ship that won the game."""
    return f"\n{ship[0]} wins this game!!!\n"


def game_setup():
    """game_setup() accepts user input, set up the data structure for the game."""
    ships_to_play = int(input("How many ships you will play: "))
    ships_to_play_against = int(input("How many ships will you play against: "))

    if ships_to_play <= 0 and ships_to_play_against <= 0:
        print("The game requires at least 2 ships to play.")
        return
    else:
        print("Enter the name of the ships you will play...")
        get_ship_name(ships_to_play, ship_list)

        print("Enter the name of the ships you will play against...")
        get_ship_name(ships_to_play_against, ship_list)


# Gameplay
welcome_screen()
game_setup()

while is_game_on:
    movement_phase(ship_list, game_round)

    proceed_to_next_phase = str(input("Proceed to the next phase [y/n]: ")).lower()
    if proceed_to_next_phase == "n":
        is_game_on = False
    else:
        attack_phase(ship_list, game_round)

        if len(ship_list) == 1:
            print(declare_victor(ship_list))
            is_game_on = False
        else:
            end_phase(game_round)
            next_round = str(input("Proceed to the next round [y/n]: ")).lower()
            if next_round == "n":
                is_game_on = False

            game_round += 1

end_screen()
