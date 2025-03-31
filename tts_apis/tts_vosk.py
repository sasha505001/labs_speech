from vosk_tts import Model, Synth
import time

# https://pypi.org/project/vosk-tts/
# Vosk TTS
# model: vosk-model-tts-ru-0.7-multi
# Языки: 
def create_vosktts_audio(text):
    model = Model(model_name="vosk-model-tts-ru-0.6-multi")
    synth = Synth(model)
    name = "vosktts_" + str(time.time() * 1000) + ".wav"
    synth.synth(text, name, speaker_id=2, noise_level=0.6667, speech_rate=1.0)
    return name


# create_vosktts_audio("ну работаем что делать")
create_vosktts_audio("what is life babe i am hurt me i hurt me myself what is life")