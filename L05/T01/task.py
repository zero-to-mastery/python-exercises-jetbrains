import sys
from random import randint

def run_game():
    # Use the command-line arguments to generate a random number in the given range
    random_number = randint(int(sys.argv[1]), int(sys.argv[2]))

    while True:
        try:
            number = int(input('Pick a number between those two you just chose: '))

            # Check that the entered number is within the range given in the command-line arguments
            if int(sys.argv[1]) <= number <= int(sys.argv[2]):
                if number == random_number:
                    print("You're a genius!")
                    break # stop the loop

        except ValueError:
            print("Please enter a number")
            continue

run_game()