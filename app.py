# Server
from flask import Flask, render_template, request, jsonify, send_file, Response
from flask_cors import CORS
# API
from tts_apis import google_tts_api
from tts_apis import pyttsx3_tts_api
# Микширование
from working_with_audio.mix_audio import centroid_mixing_async, spectral_centroid_async
# from working_with_audio.mix_audio import simple_centroid_mix_async
# Чат бот
from chatbot.openrouter_bot import openrouter_chat_async

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
    

# отправляю созданное аудио клиенту
@app.route('/generated_audios/<filename>', methods=['GET'])
def get_audio(filename):
    if not filename:
        return jsonify({"error": "No filename provided"}), 400
    else:
        path_to_file = os.getcwd() + "\\generated_audios\\" + filename
        print(path_to_file)
        return send_file(path_to_file, mimetype="audio/wav" if "wav" in filename else "audio/mp3", as_attachment=True)
    
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






