# Server
from flask import Flask, render_template, request, jsonify, send_file, Response
from flask_cors import CORS
# API
from tts_apis import google_tts_api
from tts_apis import pyttsx3_tts_api
# Микширование
from working_with_audio.mix_audio import centroid_mixing_async
# Чат бот
from chatbot.openrouter_bot import openrouter_chat_async

import time
import os
import asyncio
app = Flask(__name__)
CORS(app) # Разрешаем запросы с фронтенда (с другого домена/порта)

# список названий api а также функции в которых они реализованы, достаточно лишь имя модели и функция будет выполнена
MY_API_TTS = {
    "Google TTS": google_tts_api.gtts_audio_creator_async,
    "Pyttsx3": pyttsx3_tts_api.pyttsx3_audio_creator_async,
}

async def use_tts_my_apis(text, api_name, filename):
    if not text:
        print("Error: No text provided")
        return ""
    if api_name in MY_API_TTS:
        try:
            filename = await MY_API_TTS[api_name](text)
            print(filename)
            return filename 
        except Exception as e:
            print(f"An error occurred while using {api_name}: {e}")
            return ""
    else:
        print(f"API {api_name} не найден")
        return ""



# отправляю созданное аудио клиенту
@app.route('/generated_audios/<filename>', methods=['GET'])
def get_audio(filename):
    if not filename:
        return jsonify({"error": "No filename provided"}), 400
    else:
        path_to_file = os.getcwd() + "\\generated_audios\\" + filename
        print(path_to_file)
        return send_file(path_to_file, mimetype="audio/wav" if "wav" in filename else "audio/mp3", as_attachment=True)
    

@app.route('/')
def main_page():
    #return render_template('index.html')
    return "It's a server bro"

@app.route('/write_chatbot', methods=['POST'])
async def write_chatbot(text):
    data = request.get_json()
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    else:
        answer = await openrouter_chat_async(text)
        return jsonify({'answer': answer}), 200
    return answer

# Код для где выполняется Text-to-Speech
@app.route('/api/generate', methods=['POST'])
async def convert_text_to_speech():
    data = request.get_json()
    # извлекаю данные из запроса
    text = data.get('text')
    # print(text + '\n' + model)
    
    if not text: 
        return jsonify({'error': 'No text provided'}), 400
    try:
        # корень имени файла
        audio_name = str(time.time() * 1000)
        # генерация аудио от 2 api
        gtts_audio = await use_tts_my_apis(text, "Google TTS")
        pyttsx3_audio = await use_tts_my_apis(text, "Pyttsx3")
        # полные пути к аудио
        full_path_to_audios = os.path.join(os.getcwd(), "generated_audios")
        gtts_audio = os.path.join(full_path_to_audios, gtts_audio)
        pyttsx3_audio = os.path.join(full_path_to_audios, pyttsx3_audio)
        #print(gtts_audio, pyttsx3_audio)
        # смешиваю аудио
        mixed_audio = os.path.join(full_path_to_audios, audio_name + "_mixed.mp3")
        centroid_mixing_async(gtts_audio, pyttsx3_audio, mixed_audio)
        return jsonify({'path': audio_name}), 200
    except Exception as e:
        return jsonify({'error': str("что то пошло не так")}), 500

    


if __name__ == '__main__':
    app.run(debug=True)






