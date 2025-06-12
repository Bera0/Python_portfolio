import random

answer = random.randint(1,100)
attempts = 0
print("Select the number between 1 ~ 100")

while True:
    guess = input("Select number: ")

    if not guess.isdigit():
        print("It is not a number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < answer:
        print("Up!")
    elif guess > answer:
        print("Down!")
    else:
        print(f"Correct1 {attempts} times tried.")
        break