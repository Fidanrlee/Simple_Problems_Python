Chess = {
    'a8': 'Brook', 'b8': 'BKnight', 'c8': 'Bbishop', 'd8': 'Bking', 'e8': 'Bqueen', 'f8': 'Bbishop', 'g8': 'BKnight','h8': 'Brook',
    'a7': 'Bpawn', 'b7': 'Bpawn', 'c7': 'Bpawn', 'd7': 'Bpawn', 'e7': 'Bpawn', 'f7': 'Bpawn', 'g7': 'Bpawn','h7': 'Bpawn',
    'a6': '', 'b6': '', 'c6': '', 'd6': '', 'e6': '', 'f6': '', 'g6': '','h6': '',
    'a5': '', 'b5': '', 'c5': '', 'd5': '', 'e5': '', 'f5': '', 'g5': '','h5': '',
    'a4': '', 'b4': '', 'c4': '', 'd4': '', 'e4': '', 'f4': '', 'g4': '','h4': '',
    'a3': '', 'b3': '', 'c3': '', 'd3': '', 'e3': '', 'f3': '', 'g3': '','h3': '',
    'a2': 'Wpawn', 'b2': 'Wpawn', 'c2': 'Wpawn', 'd2': 'Wpawn', 'e2': 'Wpawn', 'f2': 'Wpawn', 'g2': 'Wpawn','h2': 'Wpawn',
    'a1': 'Wrook', 'b1': 'WKnight', 'c1': 'Wbishop', 'd1': 'Wqueen', 'e1': 'Wking', 'f1': 'Wbishop', 'g1': 'WKnight','h1': 'Wrook',
}


def isValidChessBoard(string1):
        if string1 in Chess.keys():
            return True
        else:
            return False



print(isValidChessBoard('a6'))
