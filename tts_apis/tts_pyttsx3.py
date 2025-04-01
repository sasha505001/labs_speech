import pyttsx3
import time

# https://pypi.org/project/pyttsx3/
# https://github.com/nateshmbhat/pyttsx3
# model: eSpeak NG или SAPI5
# Языки: Русский, Английский
# Работает быстро и без ошибок
def create_pyttsx3_audio(text):
    engine = pyttsx3.init()
    #engine.setProperty('voice', 'russian')  # Указываем русский голос
    name = "pytttsx3_" + str(time.time() * 1000) + ".mp3"
    engine.save_to_file(text, name)
    engine.runAndWait()
    return name

