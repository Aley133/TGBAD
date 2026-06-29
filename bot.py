import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не найден. Создай .env и добавь туда BOT_TOKEN=твой_токен")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Привет. Я TGBAD бот.\n\n"
        "Пока я умею только запускаться и отвечать.\n"
        "Следующий шаг — научим меня принимать XML и передавать его в парсер.\n\n"
        "Команды:\n"
        "/start — запуск\n"
        "/ping — проверка связи"
    )


@dp.message(Command("ping"))
async def ping_handler(message: Message):
    await message.answer("pong ✅ Бот работает")


@dp.message(F.document)
async def document_handler(message: Message):
    document = message.document

    await message.answer(
        "Файл получил ✅\n\n"
        f"Название: {document.file_name}\n"
        f"Размер: {document.file_size} байт\n\n"
        "Парсер XML подключим следующим шагом."
    )


async def main():
    print("TGBAD bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
