from gtts import gTTS
import time

# https://pypi.org/project/gTTS/
# Google TTS
# model: Google Text-to-Speech API
# Языки: Русский, Английский
def create_gtts_audio(text):
    name = "gtts_" + str(time.time() * 1000) + ".mp3"
    tts = gTTS(text=text, lang='ru')
    tts.save(name)
    return name

# проверки работоспособности
# using_google_tts("серьёзные дела")
# using_google_tts("how it's sounds in english")
# using_google_tts("hi")