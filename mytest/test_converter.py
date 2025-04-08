# тесты для проверки преобразования речевых аудиофайлов в текст
import os
from working_with_audio import converter_audio

# проверка с русским языком

# проверка с английским языком
# функция для получения всех mp3 файлов
def get_mp3_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            print(filename)


def run_tests():
    path_to_audio = os.path.join(os.getcwd(), "generated_audios")
    get_mp3_files(path_to_audio)

    for filename in os.listdir(path_to_audio):
            if filename.endswith(".mp3"):
                cur_file = os.path.join(path_to_audio, filename)
                print(cur_file)
                converter_audio.convert_mp3_to_wav(cur_file)