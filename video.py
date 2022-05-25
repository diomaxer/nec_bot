import re
import pytube
import random


def get_shedevr(folder="six_kadrov"):
    channels = ["https://www.youtube.com/user/ProstoCheloveck/featured", "https://www.youtube.com/user/JaromSP"]
    c = pytube.Channel(random.choice(channels))
    while True:
        video = random.choice(c.videos)
        if re.search(r'6 кадров', video.title.lower()):
            print(video.title)
            break
    filters = video.streams.filter(progressive=True)
    filters.get_highest_resolution().download(output_path=folder)
    file_name = re.sub(r'[.|,|"|\?|\>|\<|\:|\/|\\|\||\*]', '', video.title)
    return f"{folder}/{file_name}.mp4"
