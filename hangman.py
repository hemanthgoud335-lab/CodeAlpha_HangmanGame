import random

# 1. Create a small list of 5 predefined words
word_list = ["python", "script", "developer", "loops", "syntax"]

# 2. Pick a random word for the player to guess
secret_word = random.choice(word_list)

# 3. Set up the game variables
max_incorrect_guesses = 6
incorrect_guesses = 0
guessed_letters = []

print("Welcome to Hangman!")
print(f"The secret word has {len(secret_word)} letters.")

# 4. The Main Game Loop
while incorrect_guesses < max_incorrect_guesses:
    
    # 4a. Show the current progress of the word (e.g., p _ t h _ n)
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
            
    print(f"\nWord: {display_word}")
    print(f"Guesses left: {max_incorrect_guesses - incorrect_guesses}")
    
    # 4b. Check if the player has won (no blanks left)
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", secret_word)
        break # This stops the while loop
        
    # 4c. Ask the player for their next guess
    guess = input("Guess a single letter: ").lower()
    
    # 4d. Handle the guess logic
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
    else:
        guessed_letters.append(guess) # Add it to our list of guesses
        
        if guess not in secret_word:
            incorrect_guesses += 1
            print("Incorrect guess!")
        else:
            print("Good guess!")

# 5. Check if the player lost
if incorrect_guesses == max_incorrect_guesses:
    print("\nGame Over! You ran out of guesses.")
    print("The secret word was:", secret_word)
