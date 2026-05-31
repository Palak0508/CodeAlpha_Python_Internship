import random

def play_hangman():
    words = ['apple', 'orange', 'banana', 'grape', 'lemon']
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6
    
    print("Task 1: Hangman Game")
    
    while attempts > 0:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
                
        print("\nWord: " + display_word)
        print("Attempts left: " + str(attempts))
        
        if "_" not in display_word:
            print("You won")
            break
            
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue
            
        if guess in guessed_letters:
            print("Already guessed")
            continue
            
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print("Correct")
        else:
            attempts -= 1
            print("Wrong")
            
    if attempts == 0:
        print("Game Over. The word was: " + secret_word)

if __name__ == "__main__":
    play_hangman()