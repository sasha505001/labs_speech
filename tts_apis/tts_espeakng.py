import espeakng
import time
import os

# https://pypi.org/project/espeakng/
# model: eSpeak NG
# Языки: Английский
def create_espeakng_audio(text):
    mySpeaker = espeakng.Speaker()
    # путь к папке со сгенерированными файлами
    path = os.getcwd() + "\\generated_audios\\"
    if not os.path.exists(path):
        os.makedirs(path)
    # путь к генерируемому файлу
    filename = "espeak_" + str(time.time() * 1000) + ".mp3"
    path = path + filename
    mySpeaker.say(text, export_path=path)
    return filename