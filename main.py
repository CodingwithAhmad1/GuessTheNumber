import random
target = random.randint(1, 15)
userChoice = int(input("Guess the number: "))
guesses = 1
while userChoice != target:
    guesses = guesses + 1
    if userChoice < target:
        userChoice = int(input("Guess higher!"))
    else:
        userChoice = int(input("Guess lower!"))


print(f"It took you {guesses} guesses")
