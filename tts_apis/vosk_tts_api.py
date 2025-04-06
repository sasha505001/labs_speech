from vosk_tts import Model, Synth
import time
import os
import asyncio

# https://pypi.org/project/vosk-tts/
# Vosk TTS
# model: vosk-model-tts-ru-0.7-multi
# Языки: Русский
def vosk_audio_creator(text):
    model = Model(model_name="vosk-model-tts-ru-0.6-multi")
    synth = Synth(model)

    # путь к папке со сгенерированными файлами
    path = os.getcwd() + "\\generated_audios\\"
    if not os.path.exists(path):
        os.makedirs(path)
    # путь к генерируемому файлу
    filename = "vosktts_" + str(time.time() * 1000) + ".wav"
    path = path + filename
    synth.synth(text, path, speaker_id=2, noise_level=0.6667, speech_rate=1.0)
    return filename
# асинхронная версия
async def vosk_audio_creator_async(text):
    model = Model(model_name="vosk-model-tts-ru-0.6-multi")
    synth = Synth(model)

    # путь к папке со сгенерированными файлами
    path = os.getcwd() + "\\generated_audios\\"
    if not os.path.exists(path):
        os.makedirs(path)
    # путь к генерируемому файлу
    filename = "vosktts_" + str(time.time() * 1000) + ".wav"
    path = path + filename
    await asyncio.to_thread(synth.synth, text, path, speaker_id=2, noise_level=0.6667, speech_rate=1.0)
    return filename
