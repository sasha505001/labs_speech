import pyttsx3
import time
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor

# https://pypi.org/project/pyttsx3/
# https://github.com/nateshmbhat/pyttsx3
# model: eSpeak NG или SAPI5
# Языки: Русский, Английский
# Работает быстро и без ошибок
def pyttsx3_audio_creator(text, audio_name):
    engine = pyttsx3.init()

    # путь к папке со сгенерированными файлами
    path = os.getcwd() + "\\generated_audios\\"
    if not os.path.exists(path):
        os.makedirs(path)
    # Путь к генерируемому файлу
    filename = audio_name + "_pyttsx3.mp3"
    path = path + filename
    engine.save_to_file(text, path)
    engine.runAndWait()
    return filename

async def pyttsx3_audio_creator_async(text, audio_name):
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        filename = await loop.run_in_executor(pool, pyttsx3_audio_creator, text, audio_name)
    return filename


