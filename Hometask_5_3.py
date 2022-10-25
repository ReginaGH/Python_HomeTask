# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1,10))
game_end = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]


def drawing_lines():
    print('-'*11)
    for i in range(3):
        print('',board[0 + i*3], '|', board[1 + i*3],'|', board[2 + i*3])
        print('-'*11)

def set_position(player):
    while True:
        value = input(f'Куда рисуем {player} - ')
        if value not in '123456789':
            print('Некорректный выбор. Введите верную позицию:')
            continue
        value = int(value)
        if str(board[value-1])=='x' or str(board[value-1])=='0':
            print('Позиция занята. Выберите свободную позицию')
            continue
        board[value-1] = player
        break

def check_winner():
    for i in game_end:
        if board[i[0]-1] == board[i[1]-1] == board[i[2]-1]:
            return board[i[1]-1]
    else:
        return False

def main():
    counter = 0
    while True:
        drawing_lines()
        if counter%2==0:
            set_position('x')
        else:
            set_position('0')
        if counter > 3:
            winner = check_winner()
            if winner:
                drawing_lines()
                print('Победил:', winner)
                break
        counter+=1
        if counter > 8:
            drawing_lines()
            print('Ничья')
            break

main()
    

#     print()
#     print('-'*15)
#     result = field.copy()
#     move = move.split()
#     [x, y] = list(map(int, move))
#     if (3 > x >= 0) and (3 > y >= 0) and result[y][x] == " ":
#         result[y][x] = symbol
#     else:
#         new_attempt = input("Неправильный ход, повторите ввод: ")
#         result = make_move(field, new_attempt, symbol)
#     return result
#     # проверка ряда
#     for row in field:
#         if row[0] == "X" and row[1] == "X" and row[2] == "X":
#             return "X"
#         if row[0] == "0" and row[1] == "0" and row[2] == "0":
#             return "0"
#     # проверка колонки
#     for col in range(3):
#         if field[0][col] == "X" and field[1][col] == "X" and field[2][col] == "X":
#             return "X"
#         if field[0][col] == "0" and field[1][col] == "0" and field[2][col] == "0":
#             return "0"
#     # проверка диагонали
#     if field[0][0] == "X" and field[1][1] == "X" and field[2][2] == "X":
#         return "X"
#     if field[0][2] == "X" and field[1][1] == "X" and field[2][0] == "X":
#         return "X"
#     if field[0][0] == "0" and field[1][1] == "0" and field[2][0] == "0":
#         return "0"
#     if field[0][2] == "0" and field[1][1] == "0" and field[2][0] == "0":
#         return "0"
#     return None
#     current_player = "X" if is_X_move else "0"
#     field = make_move(field, input(
#         f"Ход игрока {current_player}: "), current_player)
#     print_field(field)
#     is_X_move = not is_X_move
#     moves_count += 1
#     print("Ничья")
#     print(f"Победитель: игрок {result}")