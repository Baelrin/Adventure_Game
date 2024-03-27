def start_game():
    name = input("Type your name: ").strip()
    print(f"Welcome {name} to this adventure!")
    return name


def choose_path():
    return (
        input(
            "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? "
        )
        .strip()
        .lower()
    )


def river_crossing():
    answer = (
        input(
            "You come to a river, you can walk around it or swim across? Type walk or swim: "
        )
        .strip()
        .lower()
    )
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")


def bridge_crossing():
    answer = (
        input(
            "You come to a bridge, it looks wobbly. Do you want to cross it or head back (cross/back)? "
        )
        .strip()
        .lower()
    )
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = (
            input(
                "You cross the bridge and meet a stranger. Do you talk to him (yes/no)? "
            )
            .strip()
            .lower()
        )
        if answer == "yes":
            print("You talk to the stranger and he gives you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended. You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")


def main():
    name = start_game()
    while True:
        path = choose_path()
        if path == "left":
            river_crossing()
        elif path == "right":
            bridge_crossing()
        else:
            print("Not a valid option. You lose.")
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break
    print(f"Thank you for trying {name}!")


if __name__ == "__main__":
    main()
