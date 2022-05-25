import re
import pytube
import random
from transliterate import translit


def get_shedevr(folder="six_kadrov"):
    channels = ["https://www.youtube.com/user/ProstoCheloveck/featured", "https://www.youtube.com/user/JaromSP"]
    c = pytube.Channel(random.choice(channels))
    while True:
        video = random.choice(c.videos)
        if re.search(r'6 кадров', video.title.lower()):
            break
    translit_name = translit(video.title.lower(), language_code='ru', reversed=True)
    file_name = re.sub(r'[.|,|"|\?|\>|\<|\:|\/|\\|\||\*]', '', translit_name)
    print(file_name)
    filters = video.streams.filter(progressive=True)
    filters.get_highest_resolution().download(output_path=folder, filename=file_name)

    return f"{folder}/{file_name}"
