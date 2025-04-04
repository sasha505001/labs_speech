import pyttsx3
import time
import os

# https://pypi.org/project/pyttsx3/
# https://github.com/nateshmbhat/pyttsx3
# model: eSpeak NG или SAPI5
# Языки: Русский, Английский
# Работает быстро и без ошибок
def create_pyttsx3_audio(text):
    engine = pyttsx3.init()

    # путь к папке со сгенерированными файлами
    path = os.getcwd() + "\\generated_audios\\"
    if not os.path.exists(path):
        os.makedirs(path)
    # Путь к генерируемому файлу
    filename = "pyttsx3_" + str(time.time() * 1000) + ".mp3"
    path = path + filename
    engine.save_to_file(text, path)
    engine.runAndWait()
    return filename

