# hangman game
import random

words = ["apple", "banana", "orange", "coconut", "pineapple"]

hangman_art = {
    0: (" ",
        " ",
        " "),
    1: (" O ",
        " ",
        " "),
    2: (" O ",
        " | ",
        " "),
    3: (" O ",
        "/| ",
        " "),
    4: (" O ",
        "/|\\",
        " "),
    5: (" O ",
        "/|\\",
        "/ "),
    6: (" O ",
        "/|\\",
        "/ \\")
}

def display_hangman(wrong_guesses):
    print("-------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("-------")

def display_hint(hint):
    print("Word: " + " ".join(hint))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True 

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        
        guess = input("Enter your guessed letter: ").lower()
        

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"'{guess}' was already guessed.")
            continue

        guessed_letters.add(guess)
            

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1 
        
    
        if "_" not in hint:
            display_hangman(wrong_guesses)
            print(f"YOU WIN! The word was: {answer}")
            is_running = False
        # 4. Fixed max attempts check
        elif wrong_guesses >= len(hangman_art) - 1:
            display_hangman(wrong_guesses)
            print(f"YOU LOSE! The word was: {answer}")
            is_running = False

if __name__ == "__main__":
    main()