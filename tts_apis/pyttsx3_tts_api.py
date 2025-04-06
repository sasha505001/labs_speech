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
def pyttsx3_audio_creator(text):
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

async def pyttsx3_audio_creator_async(text):
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        filename = await loop.run_in_executor(pool, pyttsx3_audio_creator, text)
    return filename


