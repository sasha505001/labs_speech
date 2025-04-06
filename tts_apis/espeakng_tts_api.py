import espeakng
import time
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor

# делаю функцию асинхронной 
# https://pypi.org/project/espeakng/
# model: eSpeak NG
# Языки: Английский
def espeakng_audio_creator(text):
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


# делаю функцию асинхронной(необходимо ждать создания файла)
async def espeakng_audio_creator_async(text):
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        filename = await loop.run_in_executor(pool, espeakng_audio_creator, text)
    return filename

