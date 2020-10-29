# крестики-нолики это логическая игра для двух игроков на поле 3х3 клетки
board = list(range(1,10))

won_position = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8), (3,6,9),(3,5,7)]

def draw_board():
    print ("-------------")
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
    print ("-------------")

def take_input(player_token):

    while True:
        value = input( "Игрок " + player_token + ", введите номер клетки - ")
        if not (value in '123456789'):
            print("Это не номер клетки. Итак, ваш ход - ")
            continue
        value = int(value)
        if str(board[value-1]) in 'X0':
            print("Вы можете использовать только пустые клетки")
            continue
        board[value-1] = player_token
        break

def check_win():
    for each in won_position:
        if ((board[each [0]-1]) == (board[each[1]-1]) == (board[each[2]-1])):
            return (board[each[1]-1])


def main():
    counter = 0
    while True:
        draw_board()
        if counter%2 == 0:
            take_input('X')
        else:
            take_input('0')
        if counter > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(winner, "выйграл!")
                break
        counter += 1
        if counter > 8:
                draw_board(board)
                print('Ничья!')
                break
main()

