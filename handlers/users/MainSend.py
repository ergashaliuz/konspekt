from aiogram import types

from loader import dp
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
# Echo bot
@dp.message_handler(commands="start")
async def send(message: Message):
    await message.answer("*Salom men orqali osongina konspekt qila olasiz shunchaki menga matn yuboring*",parse_mode="markdown")