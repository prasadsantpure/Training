import random

# The computer picks a random number between 1 and 10 (inclusive)
secret_number = random.randint(1, 10)

# Initialize the guess variable to something that is not the secret number
guess = None

print("Welcome to the Guess the Number Game!")
print("I have picked a number between 1 and 10. Try to guess it.")

# Loop until the user's guess is correct
while guess != secret_number:
    # Get user input and convert it to an integer
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    # Check the guess and provide feedback using conditional statements (if/elif/else)
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} correctly.")

