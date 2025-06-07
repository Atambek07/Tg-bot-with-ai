pip install aiogram openai
import openai
import asyncio
from aiogram import Bot, Dispatcher, types

# 🔑 Вставь свои API-ключи
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
openai.api_key = OPENAI_API_KEY

# 📌 Функция для получения ответа от OpenAI
async def get_ai_response(prompt):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
  )
  return response["choices"][0]["message"]["content"]

# 📌 Обработчик сообщений
@dp.message_handler()
async def handle_message(message: types.Message):
  user_text = message.text
  ai_response = await get_ai_response(user_text)
  await message.reply(ai_response)

# 📌 Запуск бота
async def main():
  await dp.start_polling()

asyncio.run(main())
