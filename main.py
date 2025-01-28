import random 

from hangman_art_module import stages,logo
from words import word_list

lives = 6 

print(logo)

# We want to randomly chose a word from our word list
chosen_word = random.choice(word_list)
print(chosen_word)

# Create a place holder to hold the random word that was chosen. _ will hold the place of each letter.
place_holder = " "
word_length = len(chosen_word)
for poasition in range(word_length):
    place_holder += "_"
print("Word to guess:" + place_holder)

# Creating a while loop will loop over the guesses and check to see if there are true or not.
# We are executing code incase the guess given in the input is true.
game_over = False 
correct_letter = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letter:
        print(f"You have already guessed {guess}")

    display = " "
    
    # We create a for loop that checks every letter in the chosen word variable.
    # If the letter is equal to the guess we display the letter and append it to the correct letter list.
    for letter in chosen_word:
        if letter == guess:
            display += letter 
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter 
        else:
            display += "_"

    
    print("Word to guess: " + display)

    # Now we are exectuing code incase the guess given is not in the chosen_word variable.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        
        if lives == 0:
            game_over = True 

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

        if "_" not in display:
            game_over = True 

            print("****************************YOU WIN****************************")


        print(stages[lives])

        