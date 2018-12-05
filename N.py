for row in range(9):
    for col in range(9):
        if col==0 or col==8 or (row==col and (col>0 and col<8)):
            print("*",end="")
        else:
            print(end=" ")
    print()