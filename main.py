import random
import time

from ascii_art import logo
print(logo)
print("Can you survive?\n")

game_over = False

from Hangman_Words import word_list

hidden_word = random.choice(word_list)

lives = 6
# print(hidden_word)

from ascii_art import stages

display = []
for letter in hidden_word:
    display += "_"
print(display)

while game_over != True:
    guess = input("Guess a letter:\n ").lower()
    for position in range(len(hidden_word)):
        letter = hidden_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in hidden_word:
        print(f"You've guess {guess}, which is not in the word.")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!")
            print(f"The word was {hidden_word}")

    print(display)
    if "_" not in display:
        game_over = True
        print("You Win!")

    print(stages[lives])