from string import punctuation
from googletrans import Translator

file_name = ""
locale = ""

assert(file_name != "" and locale != "") 

translator = Translator()
with open("words/file_name") as file_from:
    file_to = open("words/filename.txt", "w", encoding='utf-8')
    lines_number = 183
    for i, line in enumerate(file_from.readlines()):
        translation = translator.translate(line.strip(), dest=locale)
        text = str(translation.text).capitalize().strip(punctuation)
        print(f"{str(translation.origin).ljust(15)} --> {text.ljust(15)} : {'{:.2f}'.format((i/lines_number) * 100)}%")
        file_to.write(text + '\n')