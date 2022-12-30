from aiogram import types
from translate import Translator
from bot_config import *
import func_translator_text as ftt
import aiogram


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    print(message)
    await message.reply(f"Hi, {message.from_user.first_name}!\nI'm TranslatorBot!\nYou send me choised mode translate:\n /rusEn - с русского на аглийский\n /enRus - c английского на русcкий")


@dp.message_handler(commands=['rusEn', 'enRus'])
async def choise_mode(message: types.Message):

    if message.text == '/rusEn':
        ftt.translator = Translator(from_lang='ru', to_lang='en')
    else:
        ftt.translator = Translator(from_lang='en', to_lang='ru')
    await message.reply('setting is save.\n If you want to change the settings:\n /rusEn - с русского на аглийский\n /enRus - c английского на русcкий')


@dp.message_handler()
async def translate_echo(message: types.Message):
    translated_message = message.text + \
        ' - переводится как: ' + ftt.translate(message.text)
    await message.answer(translated_message)


@dp.message_handler(content_types='voice')
async def voice_echo(message: types.Message):
    await bot.send_voice(message.voice)
