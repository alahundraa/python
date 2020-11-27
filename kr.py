
X = 'X'
O = '0'
size_board = 9
do =' '
draw = 'Ничья'

def start(question):
    answer=None
    while answer not in ('да','нет'):
        answer = input(question).lower()
    return answer

def chips():
    first_move = start("Вы хотите быть первым, кто сделает ход \
(играть крестиками)?  ")
    if first_move =='да':
        print('Вы играете крестиками!')
        human = X
        comp = O
    else:
        print('Вы играете ноликами, ходите после меня')
        human = O
        comp = X
    return comp, human
        
def move_number(low,high):
    answer = None
    while answer not in range(low,high):
        answer = int(input("Делайте свой ход - напишите номер поля (0-8): "))
    return answer


def new_board():
    board=[]
    for i in range(size_board):
        board.append(do)
    return board

def view_board(board):
    print('\n', board[0], '|', board[1], '|', board[2])
    print('---------')
    print('\n', board[3], '|', board[4], '|', board[5])
    print('---------')
    print('\n', board[6], '|', board[7], '|', board[8], '\n')

def free_move(board):
    free_move = []
    for i in range(size_board):
        if board[i]== do:
            free_move.append(i)
    return free_move

def winner(board):
    for_win = ((0,1,2),
               (3,4,5),
               (6,7,8),
               (0,3,6),
               (1,4,7),
               (2,5,8),
               (0,4,8),
               (2,4,6))
    for i in for_win:
        if board[i[0]]==board[i[1]]==board[i[2]]!=do:
            winner=board[i[0]]
            return winner
        if do not in board:
            return draw
    return None
    
def human_move(board,human):
    free = free_move(board)
    move = None
    while move not in free:
        move = move_number(0,size_board)
        if move not in free:
            print('Поле занято. Напиши другой номер: ')
    print('Супер!')
    return move
    
def comp_move(board,comp,human):
    board = board[:]
    best_move = (4,0,2,6,8,1,3,5,7)
    print('Мой ход: ')
    for i in free_move(board):
        board[i] = comp
        if winner(board) == comp:
            print(i)
            return i
        board[i] = do
    for j in free_move(board):
        board[j] = human
        if winner(board) == human:
            print(j)
            return j
        board[j] = do
    for k in free_move(board):
        print(k)
        return k
        
def next_quer(quer):
    if quer == X:
        return O
    else:
        return X
        
def congratulation(win_ner,comp,human):
    if win_ner != draw:
        print('Собрана линия ',win_ner)
    else:
        print(draw)
    if win_ner==comp:
        print('Компьютер выиграл!')
    elif win_ner==human:
        print('Ты победил!')
    elif win_ner==draw:
        print(draw)
        
def main():
    comp,human = chips()
    quer = X
    board = new_board()
    view_board(board)
    while not winner(board):
        if quer == human:
            move = human_move(board,human)
            board[move] = human
        else:
            move = comp_move(board,comp,human)
            board[move] = comp
        view_board(board)
        quer = next_quer(quer)
    win_ner = winner(board)
    congratulation(win_ner,comp,human)

main()
input('\n Нажми Entr, чтобы выйти')
