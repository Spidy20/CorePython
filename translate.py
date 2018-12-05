import goslate
import speech_recognition as sr
from gtts import gTTS
import os


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak anything:")
    audio = r.listen(source)

try:

    text = r.recognize_google(audio)
    print("You said : {}".format(text))

    gs = goslate.Goslate()
    translatedText = gs.translate(text, 'fr')

    mp3 = gTTS(text=translatedText, lang='fr', slow=False)
    mp3.save("sample.mp3")
    os.system("sample.mp3")



except:
    print("Sorry could not recognize what you said")




