def choose_language():
    global locale_index
    print("Choose language: ")
    languages = ["English", "Polski", "Українська"]
    print(''.join('\t' + str(i+1) + '. ' + lang + '\n' for i,lang in enumerate(languages)))
    inp = int(input())
    match(inp):
        case 3: # Ukrainian
            locale_index = '_ua'
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
"Ти маєш: ", "життів.", "Хочеш зіграти знову? (Y - так): \n",
"""
==================
Вибери складність:
================== 
    1 легка (ти маєш 7 життів)
    2 середня (ти маєш 5 життів)
    3 складна (ти маєш 3 життя)
"""]
        case 2: # Polish
            locale_index = '_pl'
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
         "Masz: ", "życia.", "Czy chczesz kontynuować (Y oznacza tak): \n",
         """
==============
Wybierz poziom:
==============
    1 łatwy (będziesz miał 7 żyć)
    2 średni (będziesz miał 5 żyć)
    3 trudny (będziesz miał 3 życia)
         """
         ]
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
         "You have: ","lives.","Do you want to continue (Y for yes): \n",
"""
==============
Choose level: 
==============
    1 for easy (you will have 7 lives)
    2 for medium (you will have 5 lives)
    3 for hard (you will have 3 lives)
         """]