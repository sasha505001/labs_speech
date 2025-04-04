from gtts import gTTS
import time
import os

# https://pypi.org/project/gTTS/
# Google TTS
# model: Google Text-to-Speech API
# Языки: Русский, Английский
def create_gtts_audio(text):
    
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
