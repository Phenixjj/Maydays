import random

def start_game():
    print("Welcome to the Evil Alien Game!\n")
    print("You must destroy the alien spaceship\n")
    grid = 10
    goes = 0

    x = random.randint(0, grid)
    y = random.randint(0, grid)
    d = random.randint(0, grid)

    while goes < 4:
        try:
            x_guess = int(input("Enter the x coordinate (0 - 9) : "))
            y_guess = int(input("Enter the y coordinate (0 - 9) : "))
            d_guess = int(input("Enter the distance (1 - 9) : "))
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 9.")
            continue
        goes += 1
        if x_guess == x and y_guess == y and d_guess == d:
            print("* BOOM * - You got him !")
            return
        else:
            print("Shot was :")
            if x_guess > x:
                print("East")
            if x_guess < x:
                print("West")
            if y_guess > y:
                print("North")
            if y_guess < y:
                print("South")
            if d_guess > d:
                print("Too far")
            if d_guess < d:
                print("Not far enough")
    print("Your time has run out!")
       