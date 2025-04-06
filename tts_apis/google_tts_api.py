from gtts import gTTS
import time
import os
import asyncio

# https://pypi.org/project/gTTS/
# Google TTS
# model: Google Text-to-Speech API
# Языки: Русский, Английский
def gtts_audio_creator(text):
    tts = gTTS(text=text, lang='ru')
    # путь к папке со сгенерированными файлами
    path = os.getcwd() + "\\generated_audios\\"
    if not os.path.exists(path):
        os.makedirs(path)
    # путь к генерируемому файлу
    filename = "gtts_" + str(time.time() * 1000) + ".mp3"
    path = path + filename
    tts.save(path)
    return filename

# асинхронная копия функции
async def gtts_audio_creator_async(text):
    tts = gTTS(text=text, lang='ru')
    path = os.getcwd() + "\\generated_audios\\"
    if not os.path.exists(path):
        os.makedirs(path)
    filename = "gtts_" + str(time.time() * 1000) + ".mp3"
    path = path + filename
    await asyncio.to_thread(tts.save, path)  # Run tts.save in a separate thread
    return filename

