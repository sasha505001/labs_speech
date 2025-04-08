from pydub import AudioSegment
import os


# Конвертация mp3 в wav
def convert_mp3_to_wav(audio_file_path):
    try:
        # проверка на существование пути
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"Файл {audio_file_path} не найден")
        # конвертация mp3 в wav
        audio = AudioSegment.from_file(audio_file_path)
        # путь к новому файлу
        wav_file_path = audio_file_path.replace('.mp3', '.wav')
        audio.export(wav_file_path, format='wav')
        return wav_file_path
    except FileExistsError as e:
        print(f"File {audio_file_path} does not exist")
        return None
    except Exception as e:
        print(f"Error converting file: {e}")
        return None
    