from games import starship_takeoff, intergalactic_games, evil_alien, beat_the_bug_eyes
import cowsay


alien = r"""
    \
     \   ___/     \___
        `-._)     (_,-`
            \O _ O/
             \ - /
              `-(
               ||
              _||_
             |-..-|
             |/. \|
             |\__/|
           ._|//\\|_,
           `-((  ))-'
            __\\//__
            >_ /\ _<,
              '  '
"""

def main():
    print("Welcome to Computer Space Game!\n")
    cowsay.draw("Choose a game to play!", alien)
    print("1. Starship Takeoff")
    print("2. Intergalactic Games")
    print("3. Evil Alien")
    print("4. Beat the Bug Eyes")
    print("5. Moonlander (coming soon!)")
    print("6. Monster of Galacticon (coming soon!)")
    print("7. Alien Snipers (coming soon!)")
    print("8. Asteroid Belt (coming soon!)")
    print("9. Trip into the Future (coming soon!)")
    print("10. Death valley (coming soon!)")
    print("11. Exit")

    try:
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        main()
    match choice:
        case 1:
            starship_takeoff.start_game()
            main()
        case 2:
            intergalactic_games.start_game()
            main()
        case 3:
            evil_alien.start_game()
            main()
        case 4:
            beat_the_bug_eyes.start_game()
            main()
        case (5, 6, 7, 8, 9, 10):
            print("Coming soon!")
            main()
        case 11:
            print("Thank you for playing Computer Space Game!")
            quit()
        case _:
            print("Invalid choice! Please enter a valid choice.")
            main()

if __name__ == '__main__':
    main()