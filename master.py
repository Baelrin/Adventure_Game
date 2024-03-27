WELCOME_MESSAGE = "Welcome {name} to this adventure!"
INVALID_OPTION_MESSAGE = "Not a valid option. You lose."
PLAY_AGAIN_MESSAGE = "Would you like to play again? (yes/no): "


def get_user_input(prompt, valid_options):
    """
    Prompt the user for input until they provide a valid option.

    Parameters:
    prompt (str): The message displayed to the user.
    valid_options (list of str): A list of accepted responses.

    Returns:
    str: The user's valid input, lowercased and stripped of whitespace.
    """
    while True:
        answer = input(prompt).strip().lower()
        if answer in valid_options:
            return answer
        print(INVALID_OPTION_MESSAGE)


def start_game():
    """
    Start the game by welcoming the user and asking for their name.

    Returns:
    str: The name of the user.
    """
    name = input("Type your name: ").strip()
    print(WELCOME_MESSAGE.format(name=name))
    return name


def choose_path():
    """
    Ask the user to choose a path at a fork in the road.

    Returns:
    str: The user's choice of path.
    """
    return get_user_input(
        "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ",
        ["left", "right"],
    )


def river_crossing():
    """
    Handle the event where the user encounters a river and must choose to swim or walk around.
    """
    answer = get_user_input(
        "You come to a river, you can walk around it or swim across? Type walk or swim: ",
        ["walk", "swim"],
    )
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")


def bridge_crossing():
    """
    Handle the event where the user encounters a bridge and must decide to cross it or go back.
    Further interaction may occur based on the user's choices.
    """
    answer = get_user_input(
        "You come to a bridge, it looks wobbly. Do you want to cross it or head back (cross/back)? ",
        ["back", "cross"],
    )
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = get_user_input(
            "You cross the bridge and meet a stranger. Do you talk to him (yes/no)? ",
            ["yes", "no"],
        )
        if answer == "yes":
            print("You talk to the stranger and he gives you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended. You lose.")


def main():
    """
    The main function to start the game loop. It initiates the game, handles user choices,
    and manages game progression including repeating the game.
    """
    name = start_game()
    while True:
        path = choose_path()
        if path == "left":
            river_crossing()
        elif path == "right":
            bridge_crossing()
        play_again = get_user_input(PLAY_AGAIN_MESSAGE, ["yes", "no"])
        if play_again != "yes":
            break
    print(f"Thank you for trying {name}!")


if __name__ == "__main__":
    main()
