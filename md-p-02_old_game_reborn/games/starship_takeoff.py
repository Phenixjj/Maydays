import random

def start_game():
    print("Welcome to the Starship Takeoff Game!\n")
    gravity = random.randint(1, 20)
    weight = random.randint(1, 40)
    result = gravity * weight
    print("Gravity = ", gravity)
    count = 0
    while count < 10:
        try:
            force = int(input("Type in force :"))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        count += 1
        if force < result:
            print("Too low!")
            print("Try again!")
        elif force > result:
            print("Too high!")
            print("Try again!")
        else:
            print("Good take off!")
            return
    print("You failed")

if __name__ == "__main__":
    start_game()
