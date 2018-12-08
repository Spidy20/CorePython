import pyqrcode
import png

text='kushal'
try:
    url=pyqrcode.create(text)
    url.png('C:/Users/kusha/Pictures/AnyDesk/kushal.png',scale=5)
    print('Your PNG created')
except Exception as e:
    print(e)