# -*- coding: utf-8 -*-
from gtts import gTTS
from googletrans import Translator

# 유저에게 문장을 입력받는다.
user_input = input("번역할 텍스트를 입력하세요 : ").encode('utf-8').decode('utf-8')

# 번역할 언어를 선택한다.
selected_language = input("어떤 언어로 번역을 해드릴까요? ex_ en, la, jp")

translator = Translator()
translated_sentence = translator.translate(user_input, dest=selected_language)
print(translated_sentence.text)

text = translated_sentence.text
tts = gTTS(text, lang='ko')
tts.save("./output.mp3")