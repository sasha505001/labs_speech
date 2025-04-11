from pydub import AudioSegment
import os

def convert_to_wav(input_path, output_path=None):
    # Определяем расширение файла
    ext = os.path.splitext(input_path)[1].lower()
    
    if ext == '.mp3':
        audio = AudioSegment.from_mp3(input_path)
    elif ext == '.webm':
        audio = AudioSegment.from_file(input_path, format='webm')
    else:
        raise ValueError("Только mp3 и webm поддерживаются")

    # Если не указан выходной путь — делаем такой же, только .wav
    if not output_path:
        output_path = os.path.splitext(input_path)[0] + ".wav"
        
    # Сохраняем в wav формате
    audio.export(output_path, format="wav")
    return output_path
    #print(f"Файл сохранён: {output_path}")