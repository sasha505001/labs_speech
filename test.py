# Исходная точка для запуска тестов
import asyncio
# Импортируем тесты
from mytest import test_tts_apis
from mytest import test_converter
from mytest import test_stt
from mytest import test_audio_mix


all_tests = {
    "tts_apis": test_tts_apis.run_tests,
    "converter_audio": test_converter.run_tests,
    "speech_to_text": test_stt.run_tests, 
    "mix_audio": test_audio_mix.run_tests
}

names_of_test = list(all_tests.keys())

request_for_test = ""

for i in range(len(names_of_test)):
    request_for_test += f"{i} - {names_of_test[i]}\n"

request_for_test = request_for_test + "Введите номер теста(выше приведены варианты тестов): "
cur_test = input(request_for_test)
# проверка на корректность ввода
if cur_test.isdigit() and int(cur_test) < len(names_of_test) and int(cur_test) >= 0:
    if( int(cur_test) == 3):
        print("Тесты для TTS API")
        asyncio.run(all_tests[names_of_test[int(cur_test)]]())
    else:
        all_tests[names_of_test[int(cur_test)]]()
else:
    print("Некорректный ввод")

