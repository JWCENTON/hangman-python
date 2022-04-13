import random
import sys
from choose_language import choose_language
from hangman_pic import HANGMANPICS
from string import ascii_lowercase


def choose_level1():
    """ Asking user to choose desired level: easy, medium, hard."""
    ask_string = locale_text[0]
    level = input(ask_string)
    while not level.isdigit():
        level = input(ask_string)

    while int(level) < 1 or int(level) > 3:
            level = input(ask_string)
            while not level.isdigit():
                level = input(ask_string)
    return level

def choose_level2():
    """ Asking user to choose desired level: easy, medium, hard."""
    ask_string = locale_text[17]
                      
    level = input(ask_string)
    while not level.isdigit():
        level = input(ask_string)

    while int(level) < 1 or int(level) > 3:
            level = input(ask_string)
            while not level.isdigit():
                level = input(ask_string)
    return level

def get_file_name():
    categories = {
        1: locale_text[1],
        2: locale_text[2],
        3: locale_text[3]
    }
    categories_files = {
        1: "words\\countries-and-capitals",
        2: "words\\animals",
        3: "words\\food"
    }
    number = 0
    while True:
        print(locale_text[4])
        for i, cat in enumerate(categories.values()):
            print('\t',str(i+1) + '.',cat) 
        if not (number :=input("")).isdigit() or int(number) not in categories.keys():
            continue
        else:
            number = int(number)
            break
    return str(categories_files[number] + locale_index + '.txt')
    
def read_words_from_file1():
    """ Returns list with word pairs [country | capital]"""
    l = []
    # file_name = get_file_name()

    with open("words\\countries-and-capitals" + locale_index + '.txt', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if ' | ' in line:
                l.append(line)
            else:
                print("Lines in file in a wrong format! 'word | word2'")
                return None
    return l

def read_words_from_file2(file_name):
    """ Returns list with word pairs [country | capital]"""
    l = []
    # file_name = get_file_name()

    with open(file_name, encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            l.append(line)
    return l

def random_word1():
    """ Computer chooses random word from the countries-and-capitals file"""
    word = None
    while word == None:
        word = read_words_from_file1()

    difficulty = int(choose_level1())

    strip_line = [w.strip().split(" | ") for w in word] 

    if difficulty == 1: 
        choice = random.choice(strip_line) 
        lives = 7
        print(locale_text[5] + choice[0]) 
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


def random_word2(file_name):
    """ Computer chooses random word from the countries-and-capitals file"""
    word = read_words_from_file2(file_name)

    difficulty = int(choose_level2())

    if difficulty == 1: 
        choice = random.choice(word) 
        lives = 7
        # print('(delete) City: ' + choice[1]) - printing chosen citie by computer for testing
    elif difficulty == 2: 
        choice = random.choice(word) 
        lives = 5
        # print(choice) - printing chosen citie by computer for testing
    else: 
        choice = random.choice(word) 
        lives = 3
        # print(choice) - printing chosen citie by computer for testing
    return choice, lives

def user_letter():
    """ Get user input with option to quit"""
    user_char = input(locale_text[6]).lower()
    if user_char == 'quit':
        sys.exit(locale_text[7])
    while len(user_char) != 1:
        user_char = input(locale_text[6]).lower() 
    return user_char

    
def already_tried_letter():
    """ Validate if the typed letter is already in the tried letters"""
    global lives
    user_char = user_letter()
    while user_char in already_tried_letters:
        print(f"{locale_text[8]}{' '.join(already_tried_letters)}")
        user_char = input(locale_text[6]).lower() 
    if user_char not in word_to_guess.lower():
        lives -= 1
        print(HANGMANPICS[7-lives])
    already_tried_letters.append(user_char)
    print(f"{locale_text[8]}{' '.join(already_tried_letters)}")


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
            print(locale_text[10], lives)
            if check_win():
                print(locale_text[11])
                break
        if lives == 0:
            print(f'{locale_text[12]}{word_to_guess}\n{locale_text[13]}')    


locale_index = ''
locale_text = choose_language()

if __name__ == '__main__':
    end_game = 'y'
    while end_game == 'y':
        file_name = get_file_name()
        if  "countries-and-capitals" in file_name :
            guess = random_word1() # sample data, normally the word should be chosen from the countries-and-capitals.txt
            word_to_guess = guess[0]
            lives = guess[1]
            # display the chosen word to guess with all letters replaced by "_"
            # for example instead of "Cairo" display "_ _ _ _ _"
            print(f'{locale_text[14]}{lives} {locale_text[15]}')
            already_tried_letters = [' '] # this list will contain all the tried letters
            game()
            end_game = input(locale_text[16]).lower()
        else:
            guess = random_word2(file_name) # sample data, normally the word should be chosen from the countries-and-capitals.txt
            word_to_guess = guess[0]
            lives = guess[1]
            # display the chosen word to guess with all letters replaced by "_"
            # for example instead of "Cairo" display "_ _ _ _ _"
            print(f'{locale_text[14]}{lives} {locale_text[15]}')
            already_tried_letters = [' '] # this list will contain all the tried letters
            game()
            end_game = input(locale_text[16]).lower()
