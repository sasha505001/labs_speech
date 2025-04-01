import torch
import torchaudio
import time

# https://github.com/snakers4/silero-models
# silero
# Языки: Русский
def create_selero_audio(text):
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
    # Сохранение в файл
    filename = "silero_" + str(time.time() * 1000) + ".wav"
    torchaudio.save(filename, audio_tensor.cpu(), sample_rate=48000, format='wav')
    return filename

