import random
import sys
from hangman_pic import HANGMANPICS
from string import ascii_lowercase


def choose_language():
    print("Choose language: ")
    languages = ["English", "Polski", "Українська"]
    print(''.join('\t' + str(i+1) + '. ' + lang + '\n' for i,lang in enumerate(languages)))
    inp = int(input())
    match(inp):
        case 3: # Ukrainian
            return [
                """
==================
Вибери складність:
================== 
    1 легка (підказка: показує місто і ти маєш 7 життів)
    2 середня (підказка: відгадай країну і ти маєш 5 життів)
    3 складна (підказка: відгадай місто і ти маєш 3 життя)
""", "Міста і столиці", "Тварини", "Їжа","Вибери категорію: ", "Відгадай столицю: ",
"Вибери одну літеру: \n","Дякую за гру!","Вже використані літери: ", "Вже спробувана літера. Спробуй іншу: \n",
"Життя: ", "ПЕРЕМОГА!", "Не вдалося відгадати слово: ", "Поразка!",
"Ти маєш: ", "життів.", "Хочеш зіграти знову? (Y - так): \n"]
        case 2: # Polish
            return [
        """
==============
Wybierz poziom:
==============
    1 łatwy (podpowiedź: wyświetla kraj i będziesz miał 7 żyć)
    2 średni (podpowiedź: wyświetla kraj i będziesz miał 5 żyć)
    3 trudny (podpowiedź: wyświetla kraj i będziesz miał 3 życia)
         """, "Kraje i stolice", "Zwierzęta", "Jedzenie",
         "Wybierz kategorię: ", "Zgadnij stolicę: ",
         "Wybierz jedną literę: \n", "Dziękujemy za grę!",
         "Już wypróbowanę litery: ","Już wypróbowałeś tą literę. Wybierz inną literę: \n",
         "Życie: ", 'Wygrałeś!', "Nie odgadłeś słowa: ", "Przegrałeś!",
         "Masz: ", "życia.", "Czy chczesz kontynuować (Y oznacza tak tak): \n"]
        case _: # English
            return [
        """
==============
Choose level: 
==============
    1 for easy (hint: displays country and you will have 7 lives)
    2 for medium (hint: guess country and you will have 5 lives)
    3 for hard (hint: guess capital and you will have 3 lives)
         """, "Coutries and capitals", "Animals", "Food",
         "Choose category: ", "Guess a capital of: ",
         "Choose one letter: \n", "Thank You for playing!",
         "Already tried letters: ","You have already tried this letter. Choose another letter: \n",
         "Lives: ",'You WIN!', "You did not guess the word: ", "You LOST!",
         "You have: ","lives.","Do you want to continue (Y for yes): \n"]

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
    ask_string = locale_text[0]
                      
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
        1: "words\\countries-and-capitals.txt",
        2: "words\\animals.txt",
        3: "words\\food.txt"
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
    return categories_files[number]
    
def read_words_from_file1():
    """ Returns list with word pairs [country | capital]"""
    l = []
    # file_name = get_file_name()

    with open("words\\countries-and-capitals.txt") as file:
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

    with open(file_name) as file:
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
