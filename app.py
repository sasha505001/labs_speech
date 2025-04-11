# Server
from flask import Flask, render_template, request, jsonify, send_file, Response
from flask_cors import CORS
# API
from tts_apis import google_tts_api
from tts_apis import pyttsx3_tts_api
# Микширование
from working_with_audio.mix_audio import centroid_mixing_async, spectral_centroid_async
from working_with_audio.speech_to_text import speech_to_text_convert
from working_with_audio.verification import is_admin_voice
# Чат бот
from chatbot.openrouter_bot import openrouter_chat_async
from working_with_audio.converter_audio import convert_to_wav

import time
import os
import asyncio

app = Flask(__name__)
CORS(app) # Разрешаем запросы с фронтенда (с другого домена/порта)



@app.route('/center_of_mass/<filename>', methods=['GET'])
async def get_centr_of_mass(filename):
    if not filename:
        return jsonify({"error": "No filename provided"}), 400
    
    path_to_file = os.path.join(os.getcwd(), "generated_audios", filename)
    
    try:
        mean_centroid = await spectral_centroid_async(path_to_file)
        centroid = str(mean_centroid)
        return jsonify({"centroid": centroid}), 200
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/process_audio', methods=['POST'])
async def process_audio():
    # Получаю файл
    if 'file' not in request.files:
        return jsonify({'error': 'Нет файла'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Файл не выбран'}), 400
    
    # сохнаняю файл
    if file:
        filename = str(time.time() * 1000) + ".webm"
        full_path = os.path.join(os.getcwd(), "received_audios", 'records', filename)  # Сохранить как .webm
        file.save(full_path)
        new_audio = convert_to_wav(full_path)
        admin_path = os.path.join(os.getcwd(), "received_audios", 'admin', 'admin.wav')
        similarity = is_admin_voice(admin_path, new_audio)
        str_similarity = str(similarity)
        print(similarity)
        if similarity < 0.75:
            return jsonify({'text': 'Вы не админ', 'is_admin': False, 'similarity': str_similarity}), 200 
        # получаю текст из аудио
        text = await speech_to_text_convert(full_path)
        # я должен отправить текст который ответила нейронка 
        return jsonify({'text': text, 'is_admin': True, 'similarity': str_similarity}), 200

        
        

# отправляю созданное аудио клиенту
@app.route('/generated_audios/<filename>')
def get_generated_audio(filename):
    """Обслуживает сгенерированные аудиофайлы."""
    audio_path = os.path.join(os.getcwd(), "generated_audios", filename)  # Полный путь к файлу
    if filename.endswith('.wav'):
        mimetype = 'audio/wav'
    elif filename.endswith('.mp3'):
        mimetype = 'audio/mpeg'
    else:
        return jsonify({'error': 'Неподдерживаемый формат файла'}), 400

    return send_file(audio_path, mimetype=mimetype, as_attachment=True, download_name=filename) #Добавлен download_name
    
# Главная страница сервера
@app.route('/')
def main_page():
    #return render_template('index.html')
    return "It's a server bro"

# Запрос чатботу
@app.route('/write_chatbot', methods=['POST'])
async def write_chatbot():
    data = request.get_json()
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    else:
        answer = await openrouter_chat_async(text)
        print(answer)
        return jsonify({'answer': answer}), 200

# Код для где выполняется Text-to-Speech
@app.route('/generate/audios', methods=['POST'])
async def convert_text_to_speech():
    data = request.get_json()
    # извлекаю данные из запроса
    text = data.get('text')
    print(text)
    if not text: 
        return jsonify({'error': 'No text provided'}), 400
    try:
        # корень имени файла
        audio_name = str(time.time() * 1000)
        # генерация аудио от 2 api
        gtts_audio_name = await google_tts_api.gtts_audio_creator_async(text, audio_name)
        pyttsx3_audio_name = await pyttsx3_tts_api.pyttsx3_audio_creator_async(text, audio_name)
        # полные пути к аудио
        full_path_to_audios = os.path.join(os.getcwd(), "generated_audios")
        gtts_audio = os.path.join(full_path_to_audios, gtts_audio_name)
        pyttsx3_audio = os.path.join(full_path_to_audios, pyttsx3_audio_name)
        #print(gtts_audio, pyttsx3_audio)
        # смешиваю аудио
        mixed_audio_name = audio_name + "_mixed.mp3"
        mixed_audio = os.path.join(full_path_to_audios, mixed_audio_name)
        await centroid_mixing_async(gtts_audio, pyttsx3_audio, mixed_audio)
        all_audio_paths = [gtts_audio_name, pyttsx3_audio_name, mixed_audio_name]
        
        return jsonify({'names': all_audio_paths}), 200
    except Exception as e:
        return jsonify({'error': str("что то пошло не так")}), 500

    


if __name__ == '__main__':
    app.run(debug=True)






