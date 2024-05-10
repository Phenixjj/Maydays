import random
import math

def start_game():
    print("Welcome to the Intergalactic Games!\n")
    height = random.randint(1, 100)
    print("You must launch a satellite\n")
    print("To a height of : ", height)
    goes = 0
    while goes < 9 :
        try:
            speed_value = int(input("Enter the speed value (0 - 40000) : "))
            angle = int(input("Enter the angle (0 - 90) : "))
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 40000.")
            continue
        A = angle - math.atan(height/3) * 180 / math.pi
        V = speed_value - 3000 * math.sqrt(height+1/height)
        goes += 1
        if abs(A) < 2 and abs(V) < 100:
            print("You 've done it!")
            print("NCTV wins - Thanks to you!")
            return
        if A < -2 :
            print("Too Shallow!")
        if A > 2 :
            print("Too Steep!")
        if V < -100 :
            print("Too Slow!")
        if V > 100 :
            print("Too Fast!")
    print("You 've failed")
    print("You're fired")

if __name__ == "__main__":
    start_game()

