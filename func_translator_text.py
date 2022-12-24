from translate import Translator

translator = Translator(from_lang='ru', to_lang='en')


def translate(_text):
    return translator.translate(_text)
