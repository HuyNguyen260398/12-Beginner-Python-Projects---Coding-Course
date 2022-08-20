import random
import string
from tkinter import W
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    retries = 6

    # getting user input
    while len(word_letters) > 0 and retries > 0:
        # letters used
        print("You have used these letters: ", " ".join(used_letters))
        print(f"You have {retries} retries left")

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Type something: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                retries = retries - 1
                print("Letter is not in the word")

        elif user_letter in used_letters:
            print ("You already used that letter. Please try again")
        else:
            print ("Your letter is not in the word. Please try again")

    if retries == 0:
        print("You have no retries left. Game over")
    else:
        print("Congrat you guessed the word")

    print("The word is: ", " ".join(letter for letter in word))

hangman()

