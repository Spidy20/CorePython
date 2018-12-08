
##reading from files
# global file
file = 'file.txt'
# try:
#     f = open(file, 'r', encoding='utf-8')
#     print(f.read())
# except Exception as e:
#     print(e)


# #write in files
try:
    with open(file, 'w', encoding='utf-8') as f:
        f.write("I am Kushal Bhavsar\n")
        f.write("I want to be Millionaire\n")
        f.write("I just want collections of Cars\n")
        f.write('Just want to drive Lamborghinin at top speed\n')
except Exception as e:
    print(e)

# # ##Append in file
# try:
#     with open(file,'a',encoding='utf-8') as f:
#        f.write('hello w')
# except Exception as e:
#     print(e)