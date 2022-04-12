import random
import sys
from hangman_pic import HANGMANPICS
from string import ascii_lowercase

    
def choose_level():
    """ Asking user to choose desired level: easy, medium, hard."""
    level = input("\n==============\nChoose level: \n==============\n 1 for easy (hint: displays country and you will have 7 lives)\
        \n 2 for medium (hint: guess country and you will have 5 lives)\
        \n 3 for hard (hint: guess capital and you will have 3 lives)\n")
    while not level.isdigit():
        level = input("\n==============\nChoose level: \n==============\n 1 for easy (hint: displays country and you will have 7 lives)\
        \n 2 for medium (hint: guess country and you will have 5 lives)\
        \n 3 for hard (hint: guess capital and you will have 3 lives)\n")

    while int(level) < 1 or int(level) > 3:
            level = input("\n==============\nChoose level: \n==============\n 1 for easy (hint: displays country and you will have 7 lives)\
        \n 2 for medium (hint: guess country and you will have 5 lives)\
        \n 3 for hard (hint: guess capital and you will have 3 lives)\n")
            while not level.isdigit():
                level = input("\n==============\nChoose level: \n==============\n 1 for easy (hint: displays country and you will have 7 lives)\
        \n 2 for medium (hint: guess country and you will have 5 lives)\
        \n 3 for hard (hint: guess capital and you will have 3 lives)\n")
    return level


def read_words_from_file():
    """ Returns list with word pairs [country | capital]"""
    l = []
    with open('countries-and-capitals.txt') as file:
        l = file.readlines()
    for i in range(len(l)):
        l[i] = l[i][:-1] # Delete \n from word pair
    return l


def random_word():
    """ Computer chooses random word from the countries-and-capitals file"""
    word = read_words_from_file() 
    difficulty = int(choose_level())

    strip_line = [w.strip().split(" | ") for w in word] 

    if difficulty == 1: 
        choice = random.choice(strip_line) 
        lives = 7
        print('Guess a capital of: ' + choice[0]) 
        # print('(delete) City: ' + choice[1]) - printing chosen citie by computer for testing
        choice = choice[1]
    elif difficulty == 2: 
        choice = random.choice(strip_line)[0] 
        lives = 5
        # print(choice) - printing chosen citie by computer for testing
    else: 
        choice = random.choice(strip_line)[1] 
        lives = 3
        # print(choice) - printing chosen citie by computer for testing
    return choice, lives


def user_letter():
    """ Get user input with option to quit"""
    user_char = input('Choose one letter: \n').lower()
    if user_char == 'quit':
        sys.exit('Thank You for playing!')
    while len(user_char) != 1:
        user_char = input('Choose one letter: \n').lower() 
    return user_char

    
def already_tried_letter():
    """ Validate if the typed letter is already in the tried letters"""
    global lives
    user_char = user_letter()
    while user_char in already_tried_letters:
        print(f"Already tried letters: {' '.join(already_tried_letters)}")
        user_char = input('You have already tried this letter. Choose another letter: \n').lower() 
    if user_char not in word_to_guess.lower():
        lives -= 1
        print(HANGMANPICS[7-lives])
    already_tried_letters.append(user_char)
    print(f"Already tried letters: {' '.join(already_tried_letters)}")


def print_word():
    for let in word_to_guess:
        if let.lower() in already_tried_letters:
            print(let, end='')
        else:
            print('-', end='')
    print()


def check_win():    
    for char in word_to_guess:
        if char.lower() in already_tried_letters:
            continue
        else:
            return False
    return True


def game():
        while lives > 0:
            # print(word_to_guess) for testing only
            print_word()
            already_tried_letter()
            print('Lives:', lives)
            if check_win():
                print('You WIN!')
                break
        if lives == 0:
            print(f'You did not guess the word: {word_to_guess}\nYou LOST!')    


if __name__ == '__main__':
    end_game = 'y'
    while end_game == 'y':
        guess = random_word() # sample data, normally the word should be chosen from the countries-and-capitals.txt
        word_to_guess = guess[0]
        lives = guess[1]
        # display the chosen word to guess with all letters replaced by "_"
        # for example instead of "Cairo" display "_ _ _ _ _"
        print(f'You have {lives} lives.')
        already_tried_letters = [' '] # this list will contain all the tried letters
        game()
        end_game = input("Do you want to continue (Y for yes): \n").lower()
