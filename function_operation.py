eng = int(input('Enter the English marks: '))
hin = int(input('Enter the Hindi Marks: '))
maths = int(input('Enter the Maths marks'))
comp = int(input('ENter the Computer marks:'))
ss = int(input('Enter the SS marks'))

total = eng+hin+maths+comp+ss
perc = total/500*100

print('Your total Marks is :',total)
print('Your Percentage is :',perc)