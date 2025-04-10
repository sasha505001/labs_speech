import librosa
import numpy as np
from pydub import AudioSegment
import os
import asyncio

# Вычисление центроида спектра
async def spectral_centroid_async(file_path):
    # Запускаем вычисление в отдельном потоке
    def calc():
        y, sr = librosa.load(file_path)
        centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
        return np.mean(centroid)
    return await asyncio.to_thread(calc)


# Асинхронное смешивание аудио на основе спектральных центроидов
async def centroid_mixing_async(file1_path, file2_path, output_file):
    # Загружаем аудиофайлы в отдельных потоках
    audio1 = await asyncio.to_thread(AudioSegment.from_file, file1_path)
    audio2 = await asyncio.to_thread(AudioSegment.from_file, file2_path)

    # Вычисляем центроиды в отдельных потоках (так как расчет может быть затратным)
    c1 = await spectral_centroid_async(file1_path)
    c2 = await spectral_centroid_async(file2_path)

    # Баланс по центроидам
    balance = c2 / (c1 + c2)

    # Смешиваем аудио тоже в потоке 
    mixed_audio = await asyncio.to_thread(audio1.overlay, audio2, position=0, gain_during_overlay=-balance)

    # Экспорт результата также делаем неблокирующим
    await asyncio.to_thread(mixed_audio.export, output_file, format="wav")

# async def simple_centroid_mix_async(file1_path, file2_path, output_file):
#     # Загружаем аудиофайлы асинхронно
#     audio1_future = asyncio.to_thread(AudioSegment.from_file, file1_path)
#     audio2_future = asyncio.to_thread(AudioSegment.from_file, file2_path)

#     # Вычисляем центроиды асинхронно
#     c1_future = spectral_centroid_async(file1_path)
#     c2_future = spectral_centroid_async(file2_path)

#     # Дожидаемся всех результатов параллельно (ускоряет выполнение)
#     audio1, audio2, c1, c2 = await asyncio.gather(audio1_future,
#                                                   audio2_future,
#                                                   c1_future,
#                                                   c2_future)

#     # Приводим к моно для корректной работы overlay и сопоставимости звука
        
#     audio2 = audio2.set_channels(1)

#     print(f"File 1 centroid: {c1:.2f} Hz")
#     print(f"File 2 centroid: {c2:.2f} Hz")

#     total_c = c1 + c2 if (c1 + c2) != 0 else 1e-6
    
#     weight_1 = c2 / total_c
#     weight_2 = c1 / total_c
#     # выполняет перевод линейного коэффициента усиления (веса) в децибелы (дБ), а если вес ≤ 0, то задает очень большое отрицательное значение.
#     gain_db_1 = 20 * np.log10(weight_1) if weight_1 > 0 else -120 
#     gain_db_2 = 20 * np.log10(weight_2) if weight_2 > 0 else -120 

#     gain_db_1 = max(gain_db_1, -20)
#     gain_db_2 = max(gain_db_2, -20)

#     print(f"Gain adjustments: File 1: {gain_db_1:.2f} dB | File 2: {gain_db_2:.2f} dB")

#     # Применяем регулировку громкости тоже в отдельных потоках 
#     adj_audio_fut_1 = asyncio.to_thread(audio1.apply_gain, gain_db_1)
#     adj_audio_fut_2 = asyncio.to_thread(audio2.apply_gain, gain_db_2)

#     adj_audio_1, adj_audio_2 = await asyncio.gather(adj_audio_fut_1,
#                                                     adj_audio_fut_2)

    
#     # Сведение — тоже запускаем в отдельном потоке на всякий случай  
#     mixed_audio = await asyncio.to_thread(adj_audio_1.overlay,
#                                           adj_audio_2)

    
#      # Экспорт результата неблокирующе   
#     await asyncio.to_thread(mixed_audio.export,
#                             output_file,
#                             format="wav")