from random import randint

# Your task is to copy the code from `initial_solution.py` here
# and refactor it into a more testable structure.

# Move the guess-checking logic into a `run_guess` function with parameters guess and answer.
# Also add a check so that if guess is a string, the function returns False.
def run_guess(guess, answer):
    if not isinstance(guess, int):
        print('please enter an integer, not a string')
        return False
    if  0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False

# Run the interactive game only inside the main.
if __name__ == '__main__':
    answer = randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10:'))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue

# Remember to check your solution by running the tests in `test.py`.