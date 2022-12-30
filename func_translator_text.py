import speech_recognition as sr
from translate import Translator
import pyttsx3

vioce_engine = pyttsx3.init()
translator = Translator(from_lang='', to_lang='')


def translate(_text):
    return translator.translate(_text)


# def command():
#     r = sr.Recognizer()

#     with sr.Microphone() as sourse:
#         print('Скажите что-то')
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(sourse, duration=1)
#         audio = r.listen(sourse)

#     try:
#         recognized_text = r.recognize_google(audio, language='en-EN')
#         print('распознано: '+recognized_text)

#     except sr.UnknownValueError:
#         talk('повторите еще раз')
#         recognazed_text = command()

#         return recognized_text
