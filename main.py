import os
import time
import telebot
import shutil

from datetime import datetime

from joke import get_joke
from video import get_shedevr


token = '5389192597:AAF2-PB6n-EXUUYWEfJImYEbrms0tZzhQNQ'


bot = telebot.TeleBot(token)


def send_video_tg(message, text):
    video = open(get_shedevr(), 'rb')
    file_name = video.name
    if text:
        bot.send_message(message.chat.id, text)
    bot.send_video(message.chat.id, video)
    print(f"{file_name} send")
    time.sleep(5)
    video.close()
    shutil.rmtree("six_kadrov", ignore_errors=True)
    print(f"six_kadrov delete")


@bot.message_handler(commands=['start'])
def start_message(message):
    while True:
        hour = datetime.now().hour

        if hour in (10, 12, 15, 18, 21, 0):
            if hour == 10:
                bot.send_message(message.chat.id, "Good morning Vietnam")
            if hour == 0:
                bot.send_message(message.chat.id, "Спокойной ночи! Вот тебе нец на сон грядущий")
            bot.send_message(message.chat.id, get_joke())
        elif hour in (13, 17):
            send_video_tg(message, "Что-то из архивов человечества")
        time.sleep(60*60)


bot.infinity_polling()