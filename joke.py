import os
import random

def get_joke():
    file_name = random.choice(os.listdir(os.path.abspath('files')))
    with open('files/' + file_name, 'r', encoding='utf-8') as file:
        dirty_text = file.readlines()
    clean_text = []
    joke = ''
    for item in dirty_text[1:]:
        if item in ['\n']:
            if joke not in ['', '\n']:
                clean_text.append(joke)
                joke = ''
            continue
        if item in ['']:
            continue
        else:
            joke += item
    message = dirty_text[0]
    return message + random.choice(clean_text)