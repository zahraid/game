import random

number = random.randint(1, 1000)
guesses = 0

while True:
    guess = int(input("Guess the number (between 1 and 1000): "))
    guesses += 1
    if guess == number:
        print("Congratulations! You guessed the number in", guesses, "guesses.")
        break
    elif guess < number:
        print("The number is greater than your guess. Try again.")
    else:
        print("The number is smaller than your guess. Try again.")
