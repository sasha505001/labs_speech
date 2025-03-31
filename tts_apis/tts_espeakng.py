import espeakng
import time

# https://pypi.org/project/espeakng/
# model: eSpeak NG
# Языки: Английский
def create_espeakng_audio(text):
    name = "espeak_" + str(time.time() * 1000) + ".mp3"
    mySpeaker = espeakng.Speaker()
    mySpeaker.say(text, export_path=name)
    return name

# generate_audio_with_espeakng("hello world")
# generate_audio_with_espeakng("hi")