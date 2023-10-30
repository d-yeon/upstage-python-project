import speech_recognition as sr

# 음성 인식 객체 생성

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    print(audio)

try:
    result = recognizer.recognize_google(audio, language='ko_KR')
    print(result)
    
except Exception as e:
    print("Speech recognition failed", e)


# if audio == '시리야':
#     # blahblah

# tabnine 자동완성 (설치 후 회원가입 하면 하루에 몇 백 문장은 무료로 사용 가능-copilot 쓰기 전 연습해보기)
# gpt와 copilot 이 너무 강력함 

