import random

# Let's assume the code is a random 3-digit number
code = random.randint(100, 999)
guess = -1

print("Welcome to the 3-digit code guesser!")
print("I have selected a random 3-digit code. Try to guess it!")

# Loop until the guess is correct
while guess != code:
    guess = int(input("Enter your guess: "))
    
    if guess < code:
        print("Higher!")
    elif guess > code:
        print("Lower!")
    else:
        print("Congratulations! You guessed the code: {code}")
