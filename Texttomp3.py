#
# # from gtts import gTTS
# # import os
# #
# #
# # # f=open("hello.txt","r" ,encoding = 'utf-8')
# # # a = ""
# # # for i in f.readlines():
# # #     a += i
# # #     print(i)
# # a='hello'
# # mp3=gTTS(text=a)
# # mp3.save("file.mp3")
# # os.system("file.mp3")
# import os
# from gtts import gTTS
# # The text that you want to convert to audio
# mytext = 'kushal bhavsar'
#
# # Language in which you want to convert
#
#
# # Passing the text and language to the engine,
# # here we have marked slow=False. Which tells
# # the module that the converted audio should
# # have a high speed
# myobj = gTTS(text=mytext)
#
# # Saving the converted audio in a mp3 file named
# # welcome
# myobj.save("welcome1.mp3")
#
# # Playing the converted file
# os.system("welcome1.mp3")

import os
from gtts import gTTS
tts = gTTS('hello')
tts.save('hello2.mp3')
os.system('hello2.mp3')