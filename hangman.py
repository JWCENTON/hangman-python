import random

# PART 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
difficulty = "1" # sample data, normally the user should choose the difficulty
def choose_level():
    level = input("\n==============\nChoose level: \n==============\n 1 for easy (hint: displays country and you will have 3 lives)\
        \n 2 for medium (hint: guess country and you will have 5 lives)\
        \n 3 for hard (hint: guess capital and you will have 7 lives)\n")
    while not level.isdigit():
        level = input("\n==============\nChoose level: \n==============\n 1 for easy (hint: displays country and you will have 3 lives)\
        \n 2 for medium (hint: guess country and you will have 5 lives)\
        \n 3 for hard (hint: guess capital and you will have 7 lives)\n")

    while int(level) < 1 or int(level) > 3:
            level = input("\n==============\nChoose level: \n==============\n 1 for easy (hint: displays country and you will have 3 lives)\
        \n 2 for medium (hint: guess country and you will have 5 lives)\
        \n 3 for hard (hint: guess capital and you will have 7 lives)\n")
            while not level.isdigit():
                level = input("\n==============\nChoose level: \n==============\n 1 for easy (hint: displays country and you will have 3 lives)\
        \n 2 for medium (hint: guess country and you will have 5 lives)\
        \n 3 for hard (hint: guess capital and you will have 7 lives)\n")
    return level
print(choose_level())


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
    list_of_countries = [] 
    list_of_cities = []
    for line in word:
        strip_line = line.strip().split(" | ", 1)
        list_of_countries.append(strip_line[0])
        list_of_cities.append(strip_line[1])
    if level == 1:
        choice = random.choice(list_of_cities)
        print(choice)
    elif level == 2:
        choice = random.choice(list_of_countries)
        print(choice)
    else:
        choice = random.choice(list_of_cities)
        print(choice)

random_word()
word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txt
lives = 5 # sample data, normally the lives should be chosen based on the difficulty


# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"


# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions


# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
already_tried_letters = [] # this list will contain all the tried letters


# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".


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
