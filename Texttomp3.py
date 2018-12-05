
from gtts import gTTS
import os

f=open("hello.aiml","r" ,encoding = 'utf-8')
a = ""
for i in f.readlines():
    a += i
    print(i)
mp3=gTTS(text=a, lang='en', slow=False)
mp3.save("file.mp3")
os.system("file.mp3")