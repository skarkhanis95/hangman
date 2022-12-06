import random
import hangman_art
import hangman_words
from os import system, name
# 6 stages

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# choose random word from the pre-defined list above
chosen_word = random.choice(hangman_words.word_list)
#set the length of display
len_of_display = len(chosen_word)
print(f"{chosen_word}")
print(f"{hangman_art.logo}")

#generating display
display = []
# setting wrong guess list
wrong_choices = []

for _ in range(1,len_of_display+1):
    display.append("_")
#settings of game
end_of_game = False
life_lost = False
lives = 6

#game logic
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    # check if user has already guesses this word
    if guess in display:
        print(f"You have already guesses this ({guess}) word. Please Try Again")
    else:
        for position in range(len_of_display):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        
    
    if guess not in chosen_word:
        if guess not in wrong_choices:
            print(hangman_art.stages[lives])
            lives -= 1
            wrong_choices += guess
        else:
            print(f"You already lost life for guess this letter ({guess.capitalize()})...So try again!!")
    
    
    display_upper = [let.upper() for let in display]  
    print(display_upper)
    if "_" not in display and lives > 0:
        end_of_game = True
        print("You Won!")
    elif "_" in display and lives>0:
        end_of_game = False
        #print("Try Again")
    elif "_" in display and lives < 0:
        end_of_game = True
        print("You Lost")
        
