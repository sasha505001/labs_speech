from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
import time
import os


# https://thepythoncode.com/article/convert-text-to-speech-in-python
# pip install soundfile transformers datasets sentencepiece
# model: microsoft/speecht5_tts
# Языки: Английский

# устройство где будет запускаться модель
device = "cuda" if torch.cuda.is_available() else "cpu"

def crate_microsoft_audio(text):  
    # load the processor
    processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
    # load the model
    model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts").to(device)
    # load the vocoder, that is the voice encoder
    vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan").to(device)

    # preprocess text
    inputs = processor(text=text, return_tensors="pt").to(device)

    
    # random vector, meaning a random voice
    speaker_embeddings = torch.randn((1, 512)).to(device)
    speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

    # путь к папке со сгенерированными файлами
    path = os.getcwd() + "\\generated_audios\\"
    if not os.path.exists(path):
        os.makedirs(path)
    # Путь к генерируемому файлу
    filename = "microsoft_tts_" + str(time.time() * 1000) + ".mp3"
    path = path + filename

    sf.write(path, speech.cpu().numpy(), samplerate=16000)
    return filename
