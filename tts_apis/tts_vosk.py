from vosk_tts import Model, Synth
import time

# https://pypi.org/project/vosk-tts/
# Vosk TTS
# model: vosk-model-tts-ru-0.7-multi
# Языки: Русский
def create_vosktts_audio(text):
    model = Model(model_name="vosk-model-tts-ru-0.6-multi")
    synth = Synth(model)
    name = ".\\generated_audios\\vosktts_" + str(time.time() * 1000) + ".wav"
    synth.synth(text, name, speaker_id=2, noise_level=0.6667, speech_rate=1.0)
    return name

