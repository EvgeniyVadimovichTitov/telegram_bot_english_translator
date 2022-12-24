from aiogram import types

from bot_config import *
import func_translator_text as ftt


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm TranslatorBot!\nPowered by aiogram.\nYou send me text for translate")


@dp.message_handler()
async def translate_echo(message: types.Message):
    translated_message = message.text + \
        ' перевод готов: ' + ftt.translate(message.text)
    await message.answer(translated_message)
