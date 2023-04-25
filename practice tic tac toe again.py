def tic(BOARD):
    row1="{}|{}|{}".format(BOARD[0],BOARD[1],BOARD[2])
    row2="{}|{}|{}".format(BOARD[3],BOARD[4],BOARD[5])
    row3="{}|{}|{}".format(BOARD[6],BOARD[7],BOARD[8])
    a=row1+"\n"+row2+"\n"+row3
    print(a)

BOARD=[" "]*9
while(0==0):
    n = int(input("enter the index number"))
    n=n-1
    if (BOARD[n]=='x' or BOARD[n]=='o'):
        print("space already taken")
        continue
    else:
        BOARD[n]='x'
    tic(BOARD)
    o = int(input("enter the index number"))
    o=o-1
    if (BOARD[n]=='x' or BOARD[n]=='o'):
        print("space already taken")
        continue
    else:
        BOARD[o]='o'
    tic(BOARD)
