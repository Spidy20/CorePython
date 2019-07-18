for row in range(7):
    for col in range(7):

        if row == 0 or row == 3 or row == 6 or col == 6:            #or(col==0 and (row>0 and row<6)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()
# for row in range(5):
#     for col in range(5):
#         if row == 0 or row == 4 or col == 0 or col == 4:
#             print("*",end=' ')
#         else :
#             print(end=' y ')
#     print()