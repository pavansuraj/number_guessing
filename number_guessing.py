import random
import time
def intro():
    global name
    print("May I ask you for your name?")
    name = input()  # Asks for the name
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200.")
    print("you are given five chances for guessing the number.")
    time.sleep(2)
    print("Go ahead. Guess!")
def pick():
    guesses_taken = 0
    number = random.randint(1, 200)
    while guesses_taken < 6:
        time.sleep(0.25)
        enter = input("Guess: ")
        try:
            guess = int(enter)
            if 1 <= guess <= 200:
                guesses_taken += 1
                if guesses_taken < 6:
                    if guess < number:
                        print("The guess is too low.")
                    elif guess > number:
                        print("The guess is too high.")
                    else:
                        print( f"Good job,{name}! You guessed my number in {guesses_taken} guesses!")
                        break
                    print("Try Again!")
            else:
                print("Silly Goose! That number isn't in the range! Please enter a number between 1 and 200.")
        except ValueError:
            print(f"I don't think that {enter} is a number. Sorry.")
    if guess != number:
        print(f"Nope. The number I was thinking of was {number}.")
# Main game loop
play_again = "yes"
while play_again.lower() in ["yes", "y"]:
    intro()
    pick()
    print("Do you want to play again? (yes/no)")
    play_again = input()
print("Thanks for playing! Goodbye.")
