from flask import Flask, render_template, request, jsonify, send_file, Response
from flask_cors import CORS
from tts_apis import tts_espeakng, tts_google, tts_microsoft, tts_pyttsx3, tts_silero, tts_vosk
import os
app = Flask(__name__)
CORS(app) # Разрешаем запросы с фронтенда (с другого домена/порта)

API_AND_SUPP_LANG = {
    "ESpeak NG": "en",
    "Google TTS": "en, ru",
    "Microsoft TTS": "en",
    "Pyttsx3": "en, ru",
    "Silero": "ru",
    "Vosk TTS": "ru"
}

# список названий api а также функции в которых они реализованы, достаточно лишь имя модели и функция будет выполнена
MY_API_TTS = {
    "ESpeak NG": tts_espeakng.create_espeakng_audio,
    "Google TTS": tts_google.create_gtts_audio,
    "Microsoft TTS": tts_microsoft.crate_microsoft_audio,
    "Pyttsx3": tts_pyttsx3.create_pyttsx3_audio,
    "Silero": tts_silero.create_selero_audio,
    "Vosk TTS": tts_vosk.create_vosktts_audio
}

# получаю аудио
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
    sup_lang = API_AND_SUPP_LANG[api_name]
    return jsonify({"languages": sup_lang})



def use_tts_my_apis(text, api_name):
    path_to_file = ""
    if not text:
        print("Error: No text provided")
        return ""
    if api_name in MY_API_TTS:
        try:
            filename = MY_API_TTS[api_name](text)
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
        return jsonify({"error": str(e)}), 500


# Код для где выполняется Text-to-Speech
# TODO нужно сделать чтобы при вводе языка который не поддерживается всё не останавливалось и продолжало работать
@app.route('/api/convert', methods=['POST'])
def convert_text_to_speech():
    data = request.get_json()
    # извлекаю данные из запроса
    text = data.get('text')
    model = data.get('model')
    #
    # print(text + '\n' + model)
    
    if not text: 
        return jsonify({'error': 'No text provided'}), 400
    try:
        path_to_audio = use_tts_my_apis(text, model)
        return jsonify({'path': path_to_audio}), 200
    except Exception as e:
        return jsonify({'error': str("что то пошло не так")}), 500

    
    # TODO посмотреть где смотрит файлы Python 

if __name__ == '__main__':
    app.run(debug=True)






