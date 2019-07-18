maths = float(input('Enter the MAths marks:'))
sci = int(input('Enter the science marks:'))
Hin = int(input('Enter the Hindi marks:'))
comp = int(input('Enter the Computer Marks:'))
sansk = int(input('Enter the Sanskrit Marks:'))

total = maths + sci + comp +Hin +sansk
perc = total / 500*100

print('Your Total Marks is:',total)
print('Your Percetage is :',perc)
#
outstand_perf = 90
excelent = 80
good = 70
average = 60
ni = 50
#
if perc>outstand_perf :
    print('Outstanding Perfomance')
    print('Grade: A++')

elif outstand_perf> perc > excelent:
    print('Excellent perfomance')
    print('Grade: A+')

elif excelent>perc>good:
    print('Good perfomance')
    print('Grade: A')

elif good>perc>average:
    print('Need improvement')
    print('Grade: B')

elif average>perc>ni:
    print('Bhai book bhi khol diya kar')
    print('Grade: c')

elif perc<ni:
    print('Bhai Tujse na Ho payega')
    print('Grade : FF')