import torch
import torchaudio
import time
import os
import asyncio

# https://github.com/snakers4/silero-models
# silero
# Языки: Русский
def selero_audio_creator(text):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') 
    model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language='ru',
                                     speaker='v4_ru',
                                     trust_repo=True)
    model.to(device)
    
    # Создание аудио
    audio_tensor = model.apply_tts(text=text, speaker='kseniya', sample_rate=48000)

    
    if audio_tensor.ndim == 1:
        audio_tensor = audio_tensor.unsqueeze(0)

    # путь к папке со сгенерированными файлами
    path = os.getcwd() + "\\generated_audios\\"
    if not os.path.exists(path):
        os.makedirs(path)
    # путь к генерируемому файлу
    filename = "silero_" + str(time.time() * 1000) + ".wav"
    path = path + filename
    torchaudio.save(path, audio_tensor.cpu(), sample_rate=48000, format='wav')
    return filename

async def selero_audio_creator_async(text):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') 
    model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language='ru',
                                     speaker='v4_ru',
                                     trust_repo=True)
    model.to(device)
    
    # Создание аудио
    audio_tensor = model.apply_tts(text=text, speaker='kseniya', sample_rate=48000)

    
    if audio_tensor.ndim == 1:
        audio_tensor = audio_tensor.unsqueeze(0)

    # путь к папке со сгенерированными файлами
    path = os.getcwd() + "\\generated_audios\\"
    if not os.path.exists(path):
        os.makedirs(path)
    # путь к генерируемому файлу
    filename = "silero_" + str(time.time() * 1000) + ".wav"
    path = path + filename
    # заставляюм ждать создания файла
    await asyncio.to_thread(torchaudio.save, path, audio_tensor.cpu(), sample_rate=48000, format='wav')
    return filename
