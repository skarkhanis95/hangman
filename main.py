import random

word_list = ["baboon","camel","ardvark","siddharth"]
# choose random word from the pre-defined list above
chosen_word = random.choice(word_list)
#testing code
print(f"{chosen_word}")

#generating display
display = []
len_of_display = len(chosen_word)

for a in range(1,len_of_display+1):
    display.append("_")

print(display)


# 6 stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
# use the loop to check if guessed (guess) letter matched the randomnly chosed word
    for position in range(len_of_display):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Won!")
        
