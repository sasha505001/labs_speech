# тестируемые API
from tts_apis import edge_tts_api
from tts_apis import espeakng_tts_api
from tts_apis import google_tts_api
from tts_apis import microsoft_tts_api
from tts_apis import pyttsx3_tts_api
from tts_apis import silero_tts_api
from tts_apis import vosk_tts_api

import asyncio




# TODO:Возможно можно придумать лучше тесты
# Делаю хоть какое то разделение по тестам
# тестируется отчасти вручную 
# модель генерирует аудиозаписи которые потом нужно проверять вручную

# todo неправильные тесты
# когда вводится неверный язык

MY_API_TTS_ASYNC = {
    "Edge TTS": edge_tts_api.edge_audio_creator_async,
    "Espeak NG": espeakng_tts_api.espeakng_audio_creator_async,
    "Google TTS": google_tts_api.gtts_audio_creator_async,
    "Microsoft TTS": microsoft_tts_api.microsoft_audio_creator_async,
    "Pyttsx3": pyttsx3_tts_api.pyttsx3_audio_creator_async,
    "Silero": silero_tts_api.selero_audio_creator_async,
    "Vosk TTS": vosk_tts_api.vosk_audio_creator_async
}

# Тестируются только асинхронные функции на доступных им языках

# Edge TTS
asyncio.run(MY_API_TTS_ASYNC["Edge TTS"]("Привет")) 

# Espeak NG
asyncio.run(MY_API_TTS_ASYNC["Espeak NG"]("Hello, world!"))

# Google TTS
asyncio.run(MY_API_TTS_ASYNC["Google TTS"]("Hello, world!"))
asyncio.run(MY_API_TTS_ASYNC["Google TTS"]("Привет мир!"))

# Microsoft TTS
asyncio.run(MY_API_TTS_ASYNC["Microsoft TTS"]("hello fucking world!"))

# Pyttsx3
asyncio.run(MY_API_TTS_ASYNC["Pyttsx3"]("Hello, world!"))
asyncio.run(MY_API_TTS_ASYNC["Pyttsx3"]("привет мир!"))

# Silero
asyncio.run(MY_API_TTS_ASYNC["Silero"]("Привет мир!"))

# Vosk TTS
asyncio.run(MY_API_TTS_ASYNC["Vosk TTS"]("Привет мир!"))