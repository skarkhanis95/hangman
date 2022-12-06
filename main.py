import random

word_list = ["baboon","camel","ardvark"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ")

for x in chosen_word:
    if x == guess:
        print(True)
    else:
        print(False)