from aiogram import types
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.default.Share import Share
from loader import dp

# Echo bot

@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    matn = message.text
    await message.answer_photo(f"http://apis.xditya.me/write?text={message.text}",caption='*Buyurtmangiz tayyor boldi. \n\nQayta ishlatish uchun /start bosing*',parse_mode="markdown",reply_markup=Share)
