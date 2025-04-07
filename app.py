# Server
from flask import Flask, render_template, request, jsonify, send_file, Response
from flask_cors import CORS
# API
from tts_apis import edge_tts_api
from tts_apis import espeakng_tts_api
from tts_apis import google_tts_api
from tts_apis import microsoft_tts_api
from tts_apis import pyttsx3_tts_api
from tts_apis import silero_tts_api
from tts_apis import vosk_tts_api

import os
import asyncio
app = Flask(__name__)
CORS(app) # Разрешаем запросы с фронтенда (с другого домена/порта)

API_AND_SUPP_LANG = {
    "Edge TTS": "ru",
    "Espeak NG": "en",
    "Google TTS": "en, ru",
    "Microsoft TTS": "en",
    "Pyttsx3": "en, ru",
    "Silero": "ru",
    "Vosk TTS": "ru"
}

# список названий api а также функции в которых они реализованы, достаточно лишь имя модели и функция будет выполнена
MY_API_TTS = {
    "Edge TTS": edge_tts_api.edge_audio_creator_async,
    "Espeak NG": espeakng_tts_api.espeakng_audio_creator_async,
    "Google TTS": google_tts_api.gtts_audio_creator_async,
    "Microsoft TTS": microsoft_tts_api.microsoft_audio_creator_async,
    "Pyttsx3": pyttsx3_tts_api.pyttsx3_audio_creator_async,
    "Silero": silero_tts_api.selero_audio_creator_async,
    "Vosk TTS": vosk_tts_api.vosk_audio_creator_async
}

# отправляю созданное аудио клиенту
@app.route('/generated_audios/<filename>', methods=['GET'])
def get_audio(filename):
    if not filename:
        return jsonify({"error": "No filename provided"}), 400
    else:
        path_to_file = os.getcwd() + "\\generated_audios\\" + filename
        print(path_to_file)
        return send_file(path_to_file, mimetype="audio/wav" if "wav" in filename else "audio/mp3", as_attachment=True)
    

# получаю список поддерживаемых языков для модели
@app.route('/apis/get_supported_languages/<api_name>', methods=['GET'])
def get_supported_languages(api_name):
    if api_name not in API_AND_SUPP_LANG:
        return jsonify({"error": "API not found"}), 404
    sup_lang = API_AND_SUPP_LANG[api_name]
    return jsonify({"languages": sup_lang})



async def use_tts_my_apis(text, api_name):
    path_to_file = ""
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

@app.route('/')
def main_page():
    #return render_template('index.html')
    return "It's a server bro"


# Вопрос: зачем мне передавать список моделей для обработки?(буду считать что это для теста работы сервера и клиента)
@app.route('/apis/names', methods=['GET'])
def get_api_names():
    try:
        if MY_API_TTS is None:
            return jsonify({"error": "MY_API_TTS is None"}), 500
        models = list(MY_API_TTS.keys())
        # print(models.count)
        if models is None:
            return jsonify({"error": "models is None"}), 500
        return jsonify(models), 200
    except Exception as e:
        return jsonify({"error": str(e) + "что то пошло не так"}), 500


# Код для где выполняется Text-to-Speech
# TODO нужно сделать чтобы при вводе языка который не поддерживается всё не останавливалось и продолжало работать
@app.route('/api/convert', methods=['POST'])
async def convert_text_to_speech():
    data = request.get_json()
    # извлекаю данные из запроса
    text = data.get('text')
    model = data.get('model')
    #
    # print(text + '\n' + model)
    
    if not text: 
        return jsonify({'error': 'No text provided'}), 400
    try:
        path_to_audio = await use_tts_my_apis(text, model)
        return jsonify({'path': path_to_audio}), 200
    except Exception as e:
        return jsonify({'error': str("что то пошло не так")}), 500

    
    # TODO посмотреть где смотрит файлы Python 

if __name__ == '__main__':
    app.run(debug=True)






