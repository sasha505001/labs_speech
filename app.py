from flask import Flask, render_template, request, jsonify, send_file, Response
from flask_cors import CORS
from tts_apis import tts_espeakng, tts_google, tts_microsoft, tts_pyttsx3, tts_silero, tts_vosk

app = Flask(__name__)
CORS(app) # Разрешаем запросы с фронтенда (с другого домена/порта)


# список названий api а также функции в которых они реализованы, достаточно лишь имя модели и функция будет выполнена
MY_API_TTS = {
    "ESpeak NG": tts_espeakng.create_espeakng_audio,
    "Google TTS": tts_google.create_gtts_audio,
    "Microsoft TTS": tts_microsoft.crate_microsoft_audio,
    "Pyttsx3": tts_pyttsx3.create_pyttsx3_audio,
    "Silero": tts_silero.create_selero_audio,
    "Vosk TTS": tts_vosk.create_vosktts_audio
}


def use_tts_my_apis(text, api_name):
    if api_name in MY_API_TTS:
        MY_API_TTS[api_name](text)
    else:
        print(f"API {api_name} не найден")

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
        print(models.count)
        if models is None:
            return jsonify({"error": "models is None"}), 500
        return jsonify(models), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Код для где выполняется Text-to-Speech
# TODO нужно сделать чтобы при вводе языка который не поддерживается всё не останавливалось и продолжало работать
@app.route('/api/convert', methods=['POST'])
def convert_text_to_speech():
    data = request.json
    text = data.get('text')
    language = data.get('language', 'en')
    model = data.get('model', 'default')

    if not text: 
        return jsonify({'error': 'No text provided'}), 400
    
    # TODO посмотреть где смотрит файлы Python 

if __name__ == '__main__':
    app.run(debug=True)






