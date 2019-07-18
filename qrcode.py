import pyqrcode

try:
    text = 'Kushal Bhavsar'
    ur= pyqrcode.create(text)
    ur.png('KB.png')
    import os
    os.system('KB.png')
    print('Your PNG created')
except Exception as e:
    print(e)