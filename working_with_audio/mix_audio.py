import librosa
import numpy as np
from pydub import AudioSegment
import os

# Вычисление центроида спектра
def spectral_centroid(file_path):
    y, sr = librosa.load(file_path)
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    mean_centroid = np.mean(centroid)
    return mean_centroid

# Смешивание аудио на основе центроидов 
def centroid_mixing(file1_path, file2_path, output_file):
    # Загружаем оба файла через pydub
    audio1 = AudioSegment.from_file(file1_path)
    audio2 = AudioSegment.from_file(file2_path)

    # Вычисляем спектральные центры масс
    c1 = spectral_centroid(file1_path)
    c2 = spectral_centroid(file2_path)

    # Mix audio based on centroids
    balance = c2 / (c1 + c2)
    mixed_audio = audio1.overlay(audio2, position=0, gain_during_overlay=-balance)

    mixed_audio.export(output_file, format="wav")