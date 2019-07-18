import img2pdf
with open('C:/Users/kusha/Desktop/test.pdf','wb') as f:
    f.write(img2pdf.convert('C:/Users/kusha/Desktop/chamunda.jpg'))