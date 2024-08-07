import random
a = random.randint(1, 100)
tries = 0
while True:
    guess = int(input("Guess a number from 1 to 100 inclusive: "))
    tries += 1
    if guess < a:
        print("Too low")
    elif guess > a:
        print("Too high")
    else:
        print("You're correct")
        print("Number of guesses:", tries)
        break

basefare = 5.00
stopfare = 2.50
numberstop = int(input("What number stop are you at?"))
desiredstop = int(input("What number stop do you want to go to"))
numberstopstravelled = desiredstop - numberstop
formula = stopfare * numberstopstravelled + basefare
print(formula)

score = 0
characters = input("Is your password longer than 7 characters?")
uppercase = input("Does it have an uppercase letter?")
lowercase = input("Does it have a lower case letter?")
number = input("Does it have a number?")
symbol = input("Does it have a symbol?")
if characters.lower() == "yes":
    score += 1
if uppercase.lower() == "yes":
    score += 1
if lowercase.lower() == "yes":
    score += 1
if number.lower() == "yes":
    score += 1
if symbol.lower() == "yes":
    score += 1
else:
    score += 0
if score <= 2:
    print("Weak password")
if score <= 4 and score > 2:
    print("Moderately strong password")
if score == 5:
    print("Strong password")

import random
number = random.randint(1,26)
tries = 0
lettertonumber = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
    "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19,
    "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
while True:
    guess = input("Enter the lower case letter that corresponds to the random number")
    tries += 1
    if guess in lettertonumber:
        guessnumber = lettertonumber[guess]
        if guessnumber > number:
            print("Too low")
        elif guessnumber < number:
            print("Too high")
        else:
            print("You're correct")
            print("Number of guesses:", tries)
            break
