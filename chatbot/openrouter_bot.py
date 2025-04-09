import aiohttp
import asyncio
import json
import os
import sys


if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def openrouter_chat_async(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    path = os.path.join(os.getcwd(), "chatbot", "keys.json")
    
    # Загружаем ключ из файла
    with open(path, 'r') as f:
        config = json.load(f)
    api_key = config['openrouter']
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "google/gemini-flash-1.5-8b-exp",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as response:
            try:
                data = await response.json()
                
                # Для отладки выводим полный ответ API
                #print("[DEBUG] Ответ сервера:", json.dumps(data, indent=2, ensure_ascii=False))
                
                if 'error' in data:
                    raise Exception(f"API Error: {data['error'].get('message', data['error'])}")
                
                if 'choices' not in data or not data['choices']:
                    raise Exception(f"'choices' отсутствует в ответе или пусто. Ответ сервера: {data}")
                
                return data["choices"][0]["message"]["content"]
            
            except aiohttp.ContentTypeError:
                text = await response.text()
                print("Не удалось декодировать JSON! Текст ответа:")
                print(text)
                raise

# Пример вызова функции
responce = asyncio.run(openrouter_chat_async("Привет как дела?"))
print(responce)
