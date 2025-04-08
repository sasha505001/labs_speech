# функция для генерации текста из аудио
import speech_recognition as sr
import os
from working_with_audio.converter_audio import convert_mp3_to_wav
# импорчу функцию конвертации mp3 в wav


langs_dict = {
    'ru': 'ru-RU',
    'en': 'en-US'
}

# Конвертация речи в файл
# audio_file_path - путь к аудиофайлу (только .wav и .mp3)
# language - язык распознавания речи (ru, en)
def speech_to_text_convert(audio_file_path, language='ru'):
    try:
        # Проверка на существование пути
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"Файл {audio_file_path} не найден")
        
        # если файл mp3, то конвертируем его в wav
        if audio_file_path.endswith('.mp3'):
            audio_file_path = convert_mp3_to_wav(audio_file_path)
        # Создаем объект Recognizer
        r = sr.Recognizer()
        # Открываем аудиофайл
        with sr.AudioFile(audio_file_path) as source:
            # Читаем аудиофайл
            audio = r.record(source)

        # Распознаем текст из аудиофайла
        text = r.recognize_google(audio, language=langs_dict[language])
        return text
    except FileNotFoundError:# Ловим ошибку, если файл не найден
        print(f"File {audio_file_path} not found")
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


