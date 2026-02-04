import sys
input = sys.stdin.readline

def chess_analyze():
    line = list(map(str, input().rstrip().split('/')))
    chessboard = [[1] * 8 for _ in range(8)]

    # row : 8 -> 1 순서
    # col : a -> h 순서 
    for row in range(7, -1, -1):
        #col = a,b,c,d,e,f,g,h
        col = 0
        for piece in line[row]:
            # white pawn
            if piece == 'p' and row != 7:
                if col > 0:
                    chessboard[row-1][col]


            


chess_analyze()