import librosa
import numpy as np
from pydub import AudioSegment
import os
import asyncio

# Вычисление центроида спектра
def spectral_centroid(file_path):
    y, sr = librosa.load(file_path)
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    mean_centroid = np.mean(centroid)
    return mean_centroid


# Асинхронное смешивание аудио на основе спектральных центроидов
async def centroid_mixing_async(file1_path, file2_path, output_file):
    # Загружаем аудиофайлы в отдельных потоках
    audio1 = await asyncio.to_thread(AudioSegment.from_file, file1_path)
    audio2 = await asyncio.to_thread(AudioSegment.from_file, file2_path)

    # Вычисляем центроиды в отдельных потоках (так как расчет может быть затратным)
    c1 = await asyncio.to_thread(spectral_centroid, file1_path)
    c2 = await asyncio.to_thread(spectral_centroid, file2_path)

    # Баланс по центроидам
    balance = c2 / (c1 + c2)

    # Смешиваем аудио тоже в потоке (если операция тяжелая — рекомендуется)
    mixed_audio = await asyncio.to_thread(audio1.overlay, audio2, position=0, gain_during_overlay=-balance)

    # Экспорт результата также делаем неблокирующим
    await asyncio.to_thread(mixed_audio.export, output_file, format="wav")