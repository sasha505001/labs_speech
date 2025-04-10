import os
import asyncio
from working_with_audio.mix_audio import spectral_centroid, centroid_mixing_async


async def run_tests():
    cur_path = os.getcwd()
    audio1 = os.path.join(cur_path, "mytest", "test_mix","gtts.mp3")
    print(audio1)
    audio2 = os.path.join(cur_path, "mytest", "test_mix", "pyttsx3.mp3")
    audio3 = os.path.join(cur_path, "mytest", "test_mix", "mixed.mp3")

    print(spectral_centroid(audio1))
    await centroid_mixing_async(audio1, audio2, audio3)