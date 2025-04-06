import edge_tts
import asyncio
import os
import time

# https://github.com/rany2/edge-tts
# Языки: Русский(можно и английский если выбрать нужный голос)
async def edge_audio_creator_async(text):
    try:
        communicate = edge_tts.Communicate(text=text, voice="ru-RU-SvetlanaNeural")
        # путь к папке со сгенерированными файлами
        path = os.getcwd() + "\\generated_audios\\"
        # имя сгенерированного файла
        filename = "edge_" + str(time.time() * 1000) + ".mp3"
        # полный путь
        path = path + filename
        await communicate.save(path)
        return filename
    except Exception as e:
        print(f"An error occurred while using Edge TTS: {e}")
        return None

  

