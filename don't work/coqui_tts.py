# pip install pip install TTS
# Imports
import time
import torch
from TTS.api import TTS
# какие то изменения в torch(в реках к ошибки просит добавить глобалки)
from builtins import dict
torch.serialization.add_safe_globals([dict])
from collections import defaultdict
torch.serialization.add_safe_globals([defaultdict])
from TTS.utils.radam import RAdam
torch.serialization.add_safe_globals([RAdam])

# Вопрос почему так по уебански работае эта библиотека
# хоть что делай, раньше она требовала тоолко импорта а теперь в torch нужно какие то глобальные переменные добавить

# язык: Английский
# модель: Tacotron2
# почему то ломается при слишких коротких словах(пример: "hi")
def create_coqui_audio(text):
    filename = "coqui_"+str(time.time() * 1000) + ".wav"
    coqui_tts = TTS('tts_models/en/ek1/tacotron2')
    coqui_tts.tts_to_file(text=text, file_path=filename)
    return filename

create_coqui_audio("hi")


