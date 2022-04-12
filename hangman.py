import random
import sys
from string import ascii_lowercase
# PART 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
# difficulty = "1" # sample data, normally the user should choose the difficulty
end_game = 'y'
while end_game == 'y':
    def choose_level():
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
    # STEP 2
    # based on the chosen difficulty level, set the values 
    # for the player's lives
    def read_words_from_file():
        """ Returns list with word pairs [country | capital]"""
        l = []
        with open('countries-and-capitals.txt') as file:
            l = file.readlines()
        for i in range(len(l)):
            l[i] = l[i][:-1] # Delete \n from word pair
        return l


    def random_word():
        word = read_words_from_file() 
        difficulty = int(choose_level())
    
        strip_line = [w.strip().split(" | ") for w in word] 
    
        if difficulty == 1: 
            choice = random.choice(strip_line) 
            lives = 7
            print('Guess a capital of: ' + choice[0]) 
            print('(delete) City: ' + choice[1]) 
            choice = choice[1]
        elif difficulty == 2: 
            choice = random.choice(strip_line)[0] 
            lives = 5
            print(choice) 
        else: 
            choice = random.choice(strip_line)[1] 
            lives = 3
            print(choice)
        return choice, lives


    guess = random_word() # sample data, normally the word should be chosen from the countries-and-capitals.txt
    word_to_guess = guess[0]
    lives = guess[1]
    # lives = 5 # sample data, normally the lives should be chosen based on the difficulty
    # STEP 3
    # display the chosen word to guess with all letters replaced by "_"
    # for example instead of "Cairo" display "_ _ _ _ _"
    print(f'You have {lives} lives.')
    print('Guess the word: ',len(word_to_guess) * '_')
    # STEP 4
    # ask the user to type a letter
    # here you should validate if the typed letter is the word 
    # "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
    # HINT: use the upper() or lower() built-in Python functions
    def user_letter():
        user_char = input('Choose one letter: \n').lower()
        if user_char == 'quit':
            sys.exit('Thank You for playing!')
        while len(user_char) != 1:
            user_char = input('Choose one letter: \n').lower() 
        return user_char
    # user_char = user_letter()
    # STEP 5
    # validate if the typed letter is already in the tried letters
    # HINT: search on the internet: `python if letter in list`
    # If it is not, than append to the tried letters
    # If it has already been typed, return to STEP 5. HINT: use a while loop here
    HANGMANPICS = {
    0:"""
    -----^
        |
        |
        |
        |
        |
    -------o""",

    1:"""
    -----^
    |    |
        |
        |
        |
        |
    -------o""",

    2:"""
    -----^
    |    |
    O    |
        |
        |
        |
    -------o""",

    3:"""
    -----^
    |    |
    O    |
    |    |
        |
        |
    -------+""",

    4:"""
    -----^
    |    |
    O    |
    /|    |
        |
        |
    -------o """,

    5:"""
    -----^
    |    |
    O    |
    /|\   |
        |
        |
    -------+""",

    6:"""
    -----^
    |    |
    O    |
    /|\   |
    /     |
        |
    -------o""",

    7:"""
    -----^
    |    |
    *_*   |
    /|\   |
    / \   |
        |
    -------o"""}
    already_tried_letters = [' '] # this list will contain all the tried letters
    def already_tried_letter():
        global lives
        user_char = user_letter()
        while user_char in already_tried_letters:
            user_char = input('You have already tried this letter. Choose another letter: \n').lower() 
        if user_char not in word_to_guess.lower():
            lives -= 1
            print(HANGMANPICS[7-lives])
        already_tried_letters.append(user_char)

    print(f"Already tried letters: {already_tried_letters}")
    # STEP 6
    # if the letter is present in the word iterate through all the letters in the variable
    # word_to_guess. If that letter is present in the already_tried_letters then display it,
    # otherwise display "_".
    def print_word():
        for let in word_to_guess:
            if let.lower() in already_tried_letters:
                print(let, end='')
            else:
                print('-', end='')
        print()
    # ------Test------
    def check_win():    
        for char in word_to_guess:
            if char.lower() in already_tried_letters:
                continue
            else:
                return False
        return True

    while lives > 0:
        print(word_to_guess)
        print_word()
        already_tried_letter()
        print('Lives:', lives)
        if check_win():
            print('You WIN!')
            break
    if lives == 0:
        print('You LOST!')    
    # if the letter is not present in the word decrease the value in the lives variable
    # and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
    # or draw a new beautiful one on your own.
    # STEP 7
    # check if the variable already_tried_letters already contains all the letters necessary
    # to build the value in the variable word_to_guess. If so display a winning message and exit
    # the app.
    # If you still have letters that are not guessed check if you have a non negative amount of lives
    # left. If not print a loosing message and exit the app.
    # If neither of the 2 conditions mentioned above go back to STEP 4
    end_game = input("Do you want to continue (Y for yes): \n").lower()
