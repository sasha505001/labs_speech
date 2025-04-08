from working_with_audio import speech_to_text
import os
# Тесты для проверки преобразования аудио в текст
# Думаю сделаю так, текст будет генерироваться в tts по тестам
# а тут будет в текстовом поле выводиться результат распознавания
# сравнивать конечно должен человек

# для вывода всех имён файлов в папке
def get_all_files_in_directory(directory):
    for filename in os.listdir(directory):
        print(filename)

def run_tests():
    # путь к папке со сгенерированными файлами
    path_to_audio = os.path.join(os.getcwd(), "generated_audios")

    # Вывожу список файлов в папке(в которой находятся тест)
    get_all_files_in_directory(path_to_audio)

    # Прохожу по всем файлам в папке и распознаю их
    for filename in os.listdir(path_to_audio):
        cur_file = os.path.join(path_to_audio, filename)
        print(cur_file + ": ")
        text = speech_to_text.speech_to_text_convert(cur_file) 
        print(text + "\n")




