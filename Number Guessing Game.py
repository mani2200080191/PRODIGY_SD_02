import random

def guess_the_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Try to guess it!")

    while not guessed_correctly:
        # Prompt the user to input their guess
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        
        attempts += 1

        # Compare the guess to the generated number
        if user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number {random_number} correctly in {attempts} attempts.")

if __name__ == "__main__":
    guess_the_number()
