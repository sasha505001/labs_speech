import sys
import asyncio
import g4f


# Ошибка на Windows
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def use_gpt4free(prompt):
    response = await g4f.ChatCompletion.create_async(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        stream=False,
        provider=g4f.Model.best_provider  # если хотите выбрать лучший провайдер автоматически
    )
    print(response)
    return response


# # Запускаем асинхронную функцию
# asyncio.run(use_gpt4free("привет"))