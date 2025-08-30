import random

print("🎲 Welcome to Guess the Number Game!")
print("I'm thinking of a number between 1 and 50.")

secret = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret:
        print("Too small! 📉")
    elif guess > secret:
        print("Too big! 📈")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")
        break


