import random
from clear import clear_console
from art import logo

def number_guessing_game():
    #Number List
    numbers = [n for n in range(1,101)]
   
    while True:
        clear_console()
         #Generate random number - We can also use the random.randint(1, 100) method
        random_number = random.choice(numbers)
        print(random_number)
        turns = 0

        while True:
            difficulty = input(F"{logo}\nWelcome to Guess The Number!\nSelect difficulty - Easy Mode (E) or Hard Mode (H):\n").lower()
            if difficulty == "e":
                turns = 10
                break
            elif difficulty == "h":
                turns = 5
                break
            else:
                print("Please select difficulty - 'E' for Easy Mode or 'H' for Hard Mode")

        while True:
            while True:
                guess = input(F"You have {turns} turns left - Guess a number:\n")
                try:
                    guess = int(guess)
                    break
                except ValueError:
                    print("Please provide a valid number")

            if guess == random_number:
                print(F"You win! Number was {random_number}")
                break
            elif guess > random_number:
                print("Too High")
                turns -= 1
            elif guess < random_number:
                print("Too Low")
                turns -= 1
        
        reset = input("Would you like to play again? - Yes (Y) or No (N):\n").lower()
        if reset != "y":
            print("Exiting...")
            return

number_guessing_game()