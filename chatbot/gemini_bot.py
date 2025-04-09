import google.generativeai as genai
import json
import os

def ask_gemini(prompt):
    try:
        # Загрузка ключа из файла
        path = os.path.join(os.getcwd(), "chatbot", "keys.json")
        with open(path, 'r') as f:
            config = json.load(f)
        api_key = config['gemini']
        genai.configure(api_key=api_key)

        # Выбор модели
        model = genai.GenerativeModel('models/gemini-1.5-pro-001')
        # Отправка запроса к модели
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[Ошибка] Не удалось получить ответ: {e}"


# Вывод ответа
print(ask_gemini("Привет как дела"))